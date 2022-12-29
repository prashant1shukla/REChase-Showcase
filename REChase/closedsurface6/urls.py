from django.urls import path
from . import views

app_name = 'closedsurface6'
urlpatterns = [
    path('', views.home, name='home'),
]
