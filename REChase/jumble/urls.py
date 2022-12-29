from django.urls import path
from . import views

app_name = 'jumble'
urlpatterns = [
    path('', views.home, name='home'),
]
