from django.urls import path
from . import views

app_name = 'palindrome3'
urlpatterns = [
    path('', views.home, name='home'),
]