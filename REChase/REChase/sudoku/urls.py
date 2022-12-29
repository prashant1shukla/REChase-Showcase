from django.urls import path
from . import views

app_name = 'sudoku'
urlpatterns = [
    path('', views.home, name='home'),
]
