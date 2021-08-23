from django.contrib import admin
from django.urls import path


from . import views

app_name = 'juego'
urlpatterns = [
    path('juego/', views.juego ,name='juego'),
    ]