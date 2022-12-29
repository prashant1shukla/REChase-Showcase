from django import forms


class answerForm(forms.Form):
    answer = forms.CharField(min_length=7, max_length=7, required=True)
