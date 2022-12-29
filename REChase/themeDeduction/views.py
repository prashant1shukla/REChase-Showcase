from django.shortcuts import render, redirect
from teams.models import Team, Player
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import answerForm
from .models import ThemeDeduction
from teams.decorators import team_required

THIS_LEVEL = 1


@login_required
@team_required
def home(request):
    context = {}
    user = request.user
    profile = Player.objects.get(user=user)

    team = Team.objects.get(id=profile.team.pk)

    if team.current_level != THIS_LEVEL:
        return redirect(reverse_lazy('teams:get-level'))

    question = ThemeDeduction.objects.first()
    answer = answerForm(request.POST or None)
    context['team'] = team
    context['question'] = question
    context['answer'] = answer
    if request.method == 'POST':
        if answer.is_valid():
            ans1 = answer.cleaned_data['theme'].lower()
            ans2 = answer.cleaned_data['who'].lower()

            correct_ans1, correct_ans2 = 'among us', 'imposter'
            correct_ans1_1 = 'amongus'
            if (ans1 == correct_ans1 or ans1 == correct_ans1_1) and ans2 == correct_ans2:
                question.answered()
                team.answerCorr(THIS_LEVEL, [correct_ans1, correct_ans2])
                return redirect(reverse_lazy('teams:get-level'))

            else:
                context['wrong'] = 1
                question.answered(right=0)

    return render(request, 'themeDeduction/question.html', context)
