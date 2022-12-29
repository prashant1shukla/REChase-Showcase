from django import forms


class answerForm(forms.Form):
    theme = forms.CharField(required=True)
    who = forms.CharField(required=True)
