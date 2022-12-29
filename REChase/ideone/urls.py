from django.urls import path
from . import views

app_name = 'ideone'
urlpatterns = [
    path('', views.home, name='home'),
]
