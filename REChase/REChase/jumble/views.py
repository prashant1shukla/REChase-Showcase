from django.shortcuts import render, redirect
from teams.models import Team, Player
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import answerForm
from .models import Question
from teams.decorators import team_required

THIS_LEVEL = 3


@login_required
@team_required
def home(request):
    user = request.user
    context = {}
    profile = Player.objects.get(user=user)
    team = Team.objects.get(id=profile.team.pk)

    if team.current_level != THIS_LEVEL:
        return redirect(reverse_lazy('teams:get-level'))

    question = Question.objects.all().first()
    answer = answerForm(request.POST or None)
    context['team'] = team
    context['question'] = question
    context['answer'] = answer
    correct_ans = '1729'
    if request.method == 'POST':
        if answer.is_valid():
            ans = answer.cleaned_data['answer'].lower()

            if ans == correct_ans:
                team.answerCorr(THIS_LEVEL, correct_ans)
                question.answered()
                return redirect(reverse_lazy('teams:get-level'))

            else:
                question.answered(right=0)
                context = {'team': team, 'question': question, 'answer': answer, 'wrong': 1}
                return render(request, 'jumble/question.html', context)

    return render(request, 'jumble/question.html', context)
