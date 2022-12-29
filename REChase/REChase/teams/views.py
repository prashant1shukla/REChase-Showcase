from django.shortcuts import render, redirect
from . import models
import datetime
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .decorators import team_required
from .forms import (
    TeamCreationForm,
    ProfileFillForm,
)
from .utils import makeCode
from django.conf import settings


def save_profile(backend, user, response, *args, **kwargs):
    # print(response)
    if backend.name == 'google-oauth2':
        profile = user
        try:
            Player = models.Player.objects.get(user=profile)
        except:
            Player = models.Player(user=profile)
            Player.timestamp = datetime.datetime.now()
            try:
                Player.name = response.get('name')
                Player.email = response.get('email')
            except:
                Player.name = response.get('given_name') + " " + response.get('family_name')
            Player.save()


def home(request):
    user = request.user
    if not user.is_authenticated:
        # For managing event Wait and Finish
        context = {}
        if datetime.datetime.now() < datetime.datetime(2021, 4, 4, 10, 00, 00, 701322):
            context = {'wait': 1, 'cur_time': datetime.datetime.now(),
                       'start_time': datetime.datetime(3000, 4, 4, 10, 00, 00, 701322)}
        elif datetime.datetime.now() > datetime.datetime(3000, 4, 4, 18, 00, 00, 701322):
            context['finish'] = 1
        else:
            context['started'] = 1
        return render(request, 'teams/base_menu.html', context)

    profile = models.Player.objects.get(user=user)
    if profile.phone is None:
        return redirect('teams:complete-profile')
    if profile.team is None or profile.accepted == 0:
        return render(request, 'teams/no_team.html', {})
    team = models.Team.objects.get(id=profile.team.pk)
    everyone = models.Player.objects.filter(team=team.pk)
    team_players = everyone.filter(accepted=1)
    context = {'team': team, 'profile': profile, 'players': team_players, 'max_level': settings.FINAL_LEVEL}
    if team.member_count < 2:
        applicants = everyone.filter(accepted=0)
        context['applicants'] = applicants

    # For managing event Wait and Finish  
    if datetime.datetime.now() < datetime.datetime(2021, 4, 4, 10, 00, 00, 701322):
        context['wait'] = 1
        context['cur_time'] = datetime.datetime.now()
        context['start_time'] = datetime.datetime(3000, 4, 4, 10, 00, 00, 701322)
    elif datetime.datetime.now() > datetime.datetime(3000, 4, 4, 18, 00, 00, 701322):
        context['finish'] = 1
    else:
        context['started'] = 1

    return render(request, 'teams/teamHome.html', context)


@login_required
@team_required
def get_level(request):
    user = request.user
    profile = models.Player.objects.get(user=user)

    team = models.Team.objects.get(id=profile.team.pk)
    level = team.current_level
    if level > settings.FINAL_LEVEL:
        return redirect('teams:scoreboard')

    return redirect(request.path + str(level))


@login_required
def get_team(request):
    return render(request, 'teams/no_team.html', {})


@login_required
def createTeam(request):
    context = {}
    user = request.user
    profile = models.Player.objects.get(user=user)
    if profile.phone is None:
        return redirect('teams:complete-profile')
    form = TeamCreationForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        code = makeCode()
        obj.code = code
        obj.member_count = 1
        obj.save()
        curr_user = models.Player.objects.get(user=user)
        curr_user.team = obj
        curr_user.team_code = code
        curr_user.accepted = 1
        curr_user.save()
        return redirect('teams:home')

    context['form'] = form
    return render(request, 'teams/teamCreation.html', context=context)


@login_required
def joinTeam(request):
    context = {}
    user = request.user
    profile = models.Player.objects.get(user=user)
    if profile.phone is None:
        return redirect('teams:complete-profile')
    if profile.accepted == 1 and profile.team is not None:
        return redirect('teams:home')
    if request.method == 'POST':
        code = request.POST.get('code', -1)
        team = models.Team.objects.filter(code=code).first()
        if not team:
            context['wrong_code'] = 'Invalid code entered.'
            return render(request, 'teams/teamJoin.html', context=context)
        if team.member_count >= 2:
            context['team_full'] = 'Team is full.'
            return render(request, 'teams/teamJoin.html', context=context)
        profile.team = team
        profile.team_code = team.code
        profile.accepted = 0
        profile.save()
        context['sent'] = 1
        return render(request, 'teams/no_team.html', context=context)

    return render(request, 'teams/teamJoin.html', context=context)


@login_required
def profileCompleteView(request):
    context = {}
    user = request.user
    profile = models.Player.objects.get(email=user.email)
    form = ProfileFillForm(request.POST or None)
    if form.is_valid():
        form.clean()
        profile.name = form.cleaned_data['name']
        profile.phone = form.cleaned_data['phone']
        profile.save()
        return redirect('teams:home')
    context['form'] = form
    return render(request, 'teams/createProfile.html', context)


@login_required
@team_required
def leaveTeamView(request):  # needs to be removed
    context = {}
    user = request.user
    profile = models.Player.objects.get(user=user)
    team = models.Team.objects.get(id=profile.team.pk)
    if request.method == 'POST':
        if team.member_count == 1:
            team.delete()
        else:
            team.member_count = team.member_count - 1
            team.save()
        profile.team = None
        profile.team_code = None
        profile.save()
        return redirect('teams:get-team')
    context['team'] = team
    context['profile'] = profile
    return render(request, 'teams/confirmLeave.html', context)


@login_required
def acceptTeamMateView(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('/oauth/login/google-oauth2/')

    profile = models.Player.objects.get(user=user)
    if profile.phone is None:
        return redirect(reverse_lazy('teams:complete-profile'))

    if profile.accepted == 0 or profile.team is None:
        return redirect(reverse_lazy('teams:get-team'))

    context = {}
    owner = models.Player.objects.get(user=request.user)
    team = models.Team.objects.get(pk=owner.team.id)
    applicantId = int(request.POST.get('ID'))
    verdict = request.POST.get('verdict')
    applicant = models.Player.objects.get(id=applicantId)
    if verdict == 'Reject':
        applicant.team = None
        applicant.save()
    elif verdict == 'Accept':
        if team.member_count >= 2:
            context['team_full'] = 'Team is full.'
            return redirect('teams:home')
        applicant.accepted = 1
        applicant.team_code = team.code
        applicant.save()
        team.member_count = team.member_count + 1
        team.save()
    return redirect('teams:home')


def scoreboardView(request):
    context = {'cur_time': datetime.datetime.now(), 'start_time': datetime.datetime(2021, 4, 4, 10, 00, 00, 701322)}

    cur_rank = 1
    try:
        all_teams = models.Team.objects.all()
        qs = all_teams.order_by('-score', 'timestamp')
        for pl in qs:
            pl.rank = cur_rank
            cur_rank += 1
        context['qs'] = qs
    except:
        context['wrong'] = 1
    if cur_rank == 1:
        context['wrong'] = 1
    if datetime.datetime.now() < datetime.datetime(2021, 4, 4, 10, 00, 00, 701322):
        context['wait'] = 1
    return render(request, 'teams/leaderBoard.html', context)


def rules(request):
    context = {}
    return render(request, 'teams/rules.html', context)


def playerdetail(request):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy("teams:home"))
    if not request.user.is_superuser:
        return redirect(reverse_lazy("teams:home"))
    all_players = models.Player.objects.all().order_by('-team_code', 'timestamp')
    context = {'players': all_players}
    return render(request, 'teams/playerdetail.html', context)
