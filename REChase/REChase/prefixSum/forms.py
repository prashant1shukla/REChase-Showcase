from django import forms


class answerForm(forms.Form):
    answer = forms.CharField(max_length=40, required=True)


class SampleForm(forms.Form):
    sample = forms.CharField(min_length=8, max_length=12, required=True)
