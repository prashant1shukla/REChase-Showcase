from django.urls import path
from . import views

app_name = 'guessing'
urlpatterns = [
    path('', views.home, name='home'),
]
