from . import models
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from teams.decorators import team_required
from teams.models import Team, Player

from .forms import answerForm
from .utils import makeSequence

THIS_LEVEL = 4


@login_required
@team_required
def home(request):
    user = request.user
    profile = Player.objects.get(user=user)
    team = Team.objects.get(id=profile.team.pk)

    if team.current_level != THIS_LEVEL:
        return redirect(reverse_lazy('teams:get-level'))

    if team.current_question == -1:
        que, ans = makeSequence()
        team.question = que
        team.current_question = ans
        team.save()

    question = models.question.objects.all().first()
    query = team.question
    correct_ans = "496" + str(team.current_question)
    # print(correct_ans)
    if request.method == 'POST':
        answer = answerForm(request.POST, request.FILES or None)

        if not answer.is_valid():
            ctx = {'team': team, 'question': question, 'query': query, 'answer': answer}
            return render(request, 'magicalbox/question.html', ctx)

        ans = request.POST.get('answer').lower()
        if ans == correct_ans:
            team.answerCorr(THIS_LEVEL, correct_ans)
            question.answered()
            return redirect(reverse_lazy('teams:get-level'))

        else:
            question.answered(right=0)
            ctx = {'team': team, 'question': question, 'query': query, 'answer': answer, 'wrong': 1}
            return render(request, 'magicalbox/question.html', ctx)

    answer = answerForm()
    return render(request, 'magicalbox/question.html',
                  {'team': team, 'question': question, 'query': query, 'answer': answer})
