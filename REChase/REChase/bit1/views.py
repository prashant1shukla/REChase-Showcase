from django.shortcuts import render, redirect
from . import models
from teams.models import Team, Player
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import answerForm
from teams.decorators import team_required
from .utils import solve_bit1, custom_rand

THIS_LEVEL = 5


@login_required
@team_required
def home(request):
    user = request.user
    profile = Player.objects.get(user=user)
    team = Team.objects.get(id=profile.team.pk)

    if team.current_level != THIS_LEVEL:
        return redirect(reverse_lazy('teams:get-level'))

    if team.current_question == -1:
        team.current_question = custom_rand()
        team.save()

    question = models.question.objects.all().first()
    query = team.current_question

    if request.method == 'POST':
        answer = answerForm(request.POST, request.FILES or None)

        if not answer.is_valid():
            ctx = {'team': team, 'question': question, 'query': query, 'invalid': 1, 'answer': answer}
            return render(request, 'bit1/question.html', ctx)

        ans = request.POST.get('answer').lower()
        correct_ans = solve_bit1(team.current_question)

        if ans == correct_ans:
            team.answerCorr(THIS_LEVEL, correct_ans)
            question.answered()
            return redirect(reverse_lazy('teams:get-level'))

        else:
            question.answered(right=0)
            ctx = {'team': team, 'question': question, 'query': query, 'answer': answer, 'wrong': 1}
            return render(request, 'bit1/question.html', ctx)

    answer = answerForm()
    return render(request, 'bit1/question.html', {'team': team, 'question': question, 'query': query, 'answer': answer})
