from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from teams.decorators import team_required
from teams.models import Team, Player
from .forms import answerForm, SampleForm
from .models import PrefixSum, Used
from .utils import solve, func

THIS_LEVEL = 8


@login_required
@team_required
def home(request):
    context = {}
    user = request.user
    profile = Player.objects.get(user=user)
    team = Team.objects.get(id=profile.team.pk)

    if team.current_level != THIS_LEVEL:
        return redirect(reverse_lazy('teams:get-level'))

    question = PrefixSum.objects.first()

    if team.current_question == -1:
        return redirect('teams:prefixSum:firstTime')

    answer = answerForm(request.POST or None)
    context['team'] = team
    context['profile'] = profile
    sample_name, name = str(team.question).split(',')
    context['sample_name'] = sample_name
    context['sample_ans'] = solve(sample_name)
    context['name'] = name
    context['answer'] = answer
    context['question'] = question
    corr_ans = solve(name)
    if request.method == 'POST':
        if answer.is_valid():
            ans = answer.cleaned_data['answer'].upper()
            if corr_ans == ans:

                team.answerCorr(THIS_LEVEL, corr_ans)
                question.answered(right=1)
                return redirect(reverse_lazy('teams:get-level'))

            else:
                question.answered(right=0)
                context['wrong'] = 1

    return render(request, 'prefixSum/question.html', context=context)


@login_required
@team_required
def firstTime(request):
    context = {}
    user = request.user
    profile = Player.objects.get(user=user)
    team = Team.objects.get(id=profile.team.pk)

    if team.current_level != THIS_LEVEL:
        return redirect(reverse_lazy('teams:get-level'))

    context['profile'] = profile
    context['team'] = team
    if team.current_question != -1:
        return redirect('teams:prefixSum:home')

    sample = SampleForm(request.POST or None)
    context['sample'] = sample
    if request.method == 'POST':
        if sample.is_valid():
            sample_name = sample.cleaned_data['sample'].upper()
            if (not (7 < len(sample_name) < 13)) or any(map(lambda x: not 65 <= ord(x) <= 90, sample_name)):
                context['invalid'] = 1
                return render(request, 'prefixSum/firstTime.html', context=context)

            if len(set(list(sample_name))) <= 3:
                context['invalid_variation'] = 1
                return render(request, 'prefixSum/firstTime.html', context=context)

            qs = Used.objects.filter(word__exact=sample_name)
            if len(qs) != 0:
                context['repeat'] = 1
                return render(request, 'prefixSum/firstTime.html', context)
            else:
                obj = Used(word=sample_name)
                obj.save()
            context['sample_name'] = sample_name

            sample_ans = solve(sample_name)
            context['sample_ans'] = sample_ans
            name, ans = func(sample=0)
            team.question = ','.join((name, sample_name))
            team.current_question = 1
            team.save()
            return redirect('teams:prefixSum:home')

    return render(request, 'prefixSum/firstTime.html', context)
