from django.shortcuts import render, redirect
from teams.models import Team, Player
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import answerForm
from .models import Question
from teams.decorators import team_required
from .utils import getseed, get_query

THIS_LEVEL = 11


@login_required
@team_required
def home(request):
    user = request.user
    profile = Player.objects.get(user=user)
    team = Team.objects.get(id=profile.team.pk)

    if team.current_level != THIS_LEVEL:
        return redirect(reverse_lazy('teams:get-level'))

    if team.current_question == -1:
        seed, que = getseed()
        team.current_question = seed
        team.question = que
        team.save()

    question = Question.objects.all().first()
    answer = answerForm(request.POST or None)

    query = get_query(team.current_question)
    correct_ans = team.question.lower()

    if request.method == 'POST':
        if answer.is_valid():
            ans = answer.cleaned_data['answer'].lower()

            if ans == correct_ans:
                team.answerCorr(THIS_LEVEL, correct_ans)
                question.answered()
                return redirect(reverse_lazy('teams:get-level'))

            else:
                question.answered(right=0)
                context = {'team': team, 'question': question, 'query': query, 'answer': answer, 'wrong': 1}
                return render(request, 'ideone/question.html', context)

    context = {'team': team, 'question': question, 'query': query, 'answer': answer}
    return render(request, 'ideone/question.html', context)
