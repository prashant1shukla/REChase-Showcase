from django.urls import path
from . import views

app_name = 'magicalbox'
urlpatterns = [
    path('', views.home, name='home'),
]
