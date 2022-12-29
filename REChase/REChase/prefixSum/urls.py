from django.urls import path
from . import views

app_name = 'prefixSum'
urlpatterns = [
    path('', views.home, name='home'),
    path('firstTime/', views.firstTime, name='firstTime'),
]
