from django.urls import path
from . import views

app_name = 'themeDeduction'
urlpatterns = [
    path('', views.home, name='home'),
]
