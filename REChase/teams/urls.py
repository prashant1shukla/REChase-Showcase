from django.urls import path, include
from . import views

app_name = 'teams'
urlpatterns = [
    path('', views.home, name='home'),
    path('get_team/', views.get_team, name='get-team'),
    path('create-team/', views.createTeam, name='create-team'),
    path('join-team/', views.joinTeam, name='join-team'),
    path('accept-team-mate/', views.acceptTeamMateView, name='accept-teammate'),
    path('complete-profile/', views.profileCompleteView, name='complete-profile'),
    path('scoreboard/', views.scoreboardView, name='scoreboard'),
    path('rules/', views.rules, name='rules'),
    path('playerdetail/', views.playerdetail, name='teamdetail'),

    path('chase/', views.get_level, name='get-level'),
    path('chase/1/', include('nft1.urls', namespace='nft1')),
    path('chase/2/', include('turbanNumbers.urls', namespace='turbanNumbers')),
    path('chase/3/', include('palindrome3.urls', namespace='palindrome3')),
    path('chase/4/', include('magicalbox.urls', namespace='magicalbox')),
    path('chase/5/', include('museum5.urls', namespace='meseum5')),
    path('chase/6/', include('closedsurface6.urls', namespace='closedsurface6')),
    path('chase/7/', include('wordRank.urls', namespace='wordRank')),
    path('chase/8/', include('prefixSum.urls', namespace='prefixSum')),
    path('chase/9/', include('pattern9.urls', namespace='pattern9')),
    path('chase/10/', include('ciphers.urls', namespace='ciphers')),
    path('chase/11/', include('ideone.urls', namespace='ideone')),

]
