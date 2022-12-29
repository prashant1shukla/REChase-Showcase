from django import forms

from .models import (
    Team,
    Player
)


class TeamCreationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']


class ProfileFillForm(forms.ModelForm):
    phone = forms.CharField(max_length=13, min_length=10)

    class Meta:
        model = Player
        fields = ['name', 'phone']
