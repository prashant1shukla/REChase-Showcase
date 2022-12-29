from django.urls import path
from . import views

app_name = 'ciphers'
urlpatterns = [
    path('', views.home, name='home'),
]
