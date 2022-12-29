from django import forms


class answerForm(forms.Form):
    answer = forms.CharField(min_length=8, max_length=8)
