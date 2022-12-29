from django.shortcuts import render, redirect
from teams.models import Team, Player
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import AnswerForm, SpecialForm
from .models import Cipher
from teams.decorators import team_required

THIS_LEVEL = 10
FINAL_ANSWERS = ('BABIES', 'BLAST', 'ANACONDA')


@login_required
@team_required
def home(request):
    user = request.user
    context = {}
    profile = Player.objects.get(user=user)
    team = Team.objects.get(id=profile.team.pk)

    if team.current_level != THIS_LEVEL:
        return redirect(reverse_lazy('teams:get-level'))

    if str(team.current_question) == '-1':
        team.current_question = 1
        team.save()
    q_no = team.current_question
    question = Cipher.objects.get(id=q_no)  #q_no =random
    if q_no != 6:
        answer = AnswerForm(request.POST or None)
    else:
        answer = SpecialForm(request.POST or None)
    context['answer'] = answer
    context['profile'] = profile
    context['team'] = team
    context['question'] = question
    corr_ans = question.answer.upper()
    # print(corr_ans)
    if request.method == 'POST':
        if answer.is_valid():
            if q_no == 6:
                ans1 = answer.cleaned_data['answer1'].upper()
                ans2 = answer.cleaned_data['answer2'].upper()
                ans3 = answer.cleaned_data['answer3'].upper()
                corr_ans = FINAL_ANSWERS
                ans = (ans1, ans2, ans3)
            else:
                ans = answer.cleaned_data['answer'].upper()
            if corr_ans == ans:
                question.answered(right=1)
                if q_no == 7:
                    team.answerCorr(THIS_LEVEL, corr_ans)
                    return redirect(reverse_lazy('teams:get-level'))
                else:
                    team.specialCipher(corr_ans)
                    return redirect('teams:ciphers:home')

            else:
                question.answered(right=0)
                context['wrong'] = 1

    return render(request, 'ciphers/question.html', context)
