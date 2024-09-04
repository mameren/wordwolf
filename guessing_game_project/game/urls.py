# game/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('guess/', views.guess_number, name='guess_number'),
]
