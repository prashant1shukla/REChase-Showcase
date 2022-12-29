from django.urls import path
from . import views

app_name = 'bit1'
urlpatterns = [
    path('', views.home, name='home'),
]
