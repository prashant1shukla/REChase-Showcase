from random import random
from django.shortcuts import render, redirect
from teams.models import Team, Player
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import answerForm
from .models import Question
from .utils import getques
from teams.decorators import team_required

THIS_LEVEL = 6


@login_required
@team_required
def home(request):
    context = {}
    user = request.user
    profile = Player.objects.get(user=user)
    team = Team.objects.get(id=profile.team.pk)

    cnt = Question.objects.count()
    if team.current_level != THIS_LEVEL:
        return redirect(reverse_lazy('teams:get-level'))

    question = Question.objects.all().first()
    if str(team.current_question) == '-1':
        team.current_question = getques(cnt)
        team.save()
    ques_no = team.current_question
    question = Question.objects.get(q_no=ques_no)
    answer = answerForm(request.POST or None)
    context['team'] = team
    context['question'] = question
    context['profile'] = profile
    context['answer'] = answer
    correct_ans = int(question.answer)
    if request.method == 'POST':
        if answer.is_valid():
            ans = int(answer.cleaned_data['answer'])
            if correct_ans == ans:
                team.answerCorr(THIS_LEVEL, correct_ans)
                question.answered(right=1)
                return redirect(reverse_lazy('teams:get-level'))

            else:
                question.answered(right=0)
                context['wrong'] = 1
        else:
            context['invalid'] = 1

    return render(request,'closedsurface6/question.html', context)
