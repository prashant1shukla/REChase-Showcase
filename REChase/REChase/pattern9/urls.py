from django.urls import path
from . import views

app_name = 'pattern9'
urlpatterns = [
    path('', views.home, name='home'),
]
