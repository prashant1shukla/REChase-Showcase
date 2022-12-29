from django.urls import path
from . import views

app_name = 'nft1'
urlpatterns = [
    path('', views.home, name='home'),
]
