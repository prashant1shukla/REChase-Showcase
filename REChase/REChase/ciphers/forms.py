from django import forms


class AnswerForm(forms.Form):
    answer = forms.CharField(max_length=256)


class SpecialForm(forms.Form):
    answer1=forms.CharField(max_length=64,required=True)
    answer2=forms.CharField(max_length=64,required=True)
    answer3=forms.CharField(max_length=64,required=True)
