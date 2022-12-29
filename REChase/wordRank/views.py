from django.shortcuts import render, redirect
from django.contrib.auth import models
from . import models
from teams.models import Team, Player
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import answerForm
import random
from teams.decorators import team_required
from .utils import getname, solve, compare, getquery

THIS_LEVEL = 7


@login_required
@team_required
def home(request):
    user = request.user
    profile = Player.objects.get(user=user)
    team = Team.objects.get(id=profile.team.pk)

    if team.current_level != THIS_LEVEL:
        return redirect(reverse_lazy('teams:get-level'))

    if team.current_question == -1:
        que = getname()
        team.question = que
        team.current_question = random.randint(20, 60)
        team.save()

    question = models.Question.objects.all().first()
    query = getquery(team.question, team.current_question)

    if request.method == 'POST':
        answer = answerForm(request.POST, request.FILES or None)

        if not answer.is_valid():
            ctx = {'team': team, 'question': question, 'query': query, 'answer': answer}
            return render(request, 'wordRank/question.html', ctx)

        reply = request.POST.get('answer').upper()
        correct_ans = team.current_question

        if compare(reply, team.question.split()[0]):
            ans = solve(reply)
        else:
            ans = -1

        if ans == correct_ans:
            team.answerCorr(THIS_LEVEL, correct_ans)
            question.answered(right=1)
            return redirect(reverse_lazy('teams:get-level'))

        else:
            question.answered(right=0)
            ctx = {'team': team, 'question': question, 'query': query, 'answer': answer, 'wrong': 1}
            return render(request, 'wordRank/question.html', ctx)

    answer = answerForm()
    return render(request, 'wordRank/question.html',
                  {'team': team, 'question': question, 'query': query, 'answer': answer})
