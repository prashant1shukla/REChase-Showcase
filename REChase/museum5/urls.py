from django.urls import path
from . import views

app_name = 'meseum5'
urlpatterns = [
    path('', views.home, name='home'),
]
