from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('players', views.players, name="players"),
    path('features', views.features, name="features"),
    path('contact', views.contact, name="contact"),
    path('team', views.team, name="team"),
]
