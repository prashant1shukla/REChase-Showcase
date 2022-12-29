from django.shortcuts import render, redirect
from . import models
from teams.models import Team, Player
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import answerForm
from teams.decorators import team_required
from .utils import solve, invalid_input
import random

THIS_LEVEL = 6


@login_required
@team_required
def home(request):
    user = request.user
    profile = Player.objects.get(user=user)
    team = Team.objects.get(id=profile.team.pk)

    if team.current_level != THIS_LEVEL:
        return redirect(reverse_lazy('teams:get-level'))

    if team.current_question == -1:
        team.current_question = random.randint(10000, 99999)
        team.question = "Start Guessing"
        team.save()

    question = models.Question.objects.all().first()
    query = team.question
    correct_ans = team.current_question

    if request.method == 'POST':
        answer = answerForm(request.POST, request.FILES or None)

        if not answer.is_valid():
            ctx = {'team': team, 'question': question, 'query': query, 'answer': answer}
            return render(request, 'guessing/question.html', ctx)
        ans = request.POST.get('answer').upper()

        if invalid_input(ans):
            ctx = {'team': team, 'question': question, 'query': query, 'answer': answer, 'invalid': 1}
            return render(request, 'guessing/question.html', ctx)

        if int(ans) == correct_ans:
            team.answerCorr(THIS_LEVEL, correct_ans)
            question.answered(right=1)
            return redirect(reverse_lazy('teams:get-level'))

        else:
            team.question = solve(ans, correct_ans)
            team.save()
            question.answered(right=0)
            query = team.question
            ctx = {'team': team, 'question': question, 'query': query, 'answer': answer, 'wrong': 1}
            return render(request, 'guessing/question.html', ctx)

    answer = answerForm()
    return render(request, 'guessing/question.html',
                  {'team': team, 'question': question, 'query': query, 'answer': answer})
