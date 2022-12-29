import json
import string

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from teams.decorators import team_required
from teams.models import Team, Player

from . import models, utils

THIS_LEVEL = 9


@login_required
@team_required
def home(request):
    user = request.user
    context = {}
    profile = Player.objects.get(user=user)
    team = Team.objects.get(id=profile.team.pk)

    if team.current_level != THIS_LEVEL or team.current_level > settings.FINAL_LEVEL:
        return redirect(reverse_lazy('teams:get-level'))

    question = models.Sudoku.objects.first()
    context['question'] = question
    context['prefilled'] = utils.prefilled
    n = utils.n
    total_rows = string.digits[1:n + 1]
    if team.question == '-1':
        prev_attempt = {}
    else:
        temp = json.loads(team.question)
        prev_attempt = {'{}{}'.format(i + 1, j + 1): temp[i][j] for i in range(n) for j in range(n)}
    context['totalRows'] = total_rows
    context['prevAttempt'] = prev_attempt
    if request.method == 'POST':
        p = request.POST
        prefilled = utils.prefilled
        arr = [[0] * n for _ in range(n)]
        for row in total_rows:
            for col in total_rows:
                x = row + col
                if x in prefilled:
                    temp = prefilled[x]
                else:
                    temp = p.get(x)
                if temp is None or (not str(temp).isdigit()):
                    context['invalid'] = 1
                    return render(request, 'sudoku/question.html', context)

                arr[int(row) - 1][int(col) - 1] = int(temp)
        correct_ans = arr
        if utils.masterChecker(arr):
            team.answerCorr(THIS_LEVEL, correct_ans)
            question.answered(right=1)
            context['right'] = 1
            return redirect(reverse_lazy('teams:get-level'))
        else:
            js = json.dumps(arr)
            prev_attempt = {'{}{}'.format(i + 1, j + 1): arr[i][j] for i in range(n) for j in range(n)}
            team.question = js
            context['wrong'] = 1
            question.answered(right=0)

        team.save()

    context['prevAttempt'] = prev_attempt
    return render(request, 'sudoku/question.html', context)
