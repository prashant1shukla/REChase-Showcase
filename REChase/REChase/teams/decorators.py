from .models import Player
from django.shortcuts import redirect
from django.urls import reverse_lazy
import datetime


def team_required(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect('/oauth/login/google-oauth2/')

        profile = Player.objects.get(user=user)
        if profile.phone is None:
            return redirect(reverse_lazy('teams:complete-profile'))

        if profile.accepted == 0 or profile.team is None:
            return redirect(reverse_lazy('teams:get-team'))

        if user.is_superuser:
            pass
        elif datetime.datetime.now() < datetime.datetime(2021, 4, 4, 10, 00, 00, 701322):
            return redirect('teams:home')
        elif datetime.datetime.now() > datetime.datetime(2021, 4, 4, 18, 00, 00, 701322):
            return redirect('teams:scoreboard')

        return function(request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
