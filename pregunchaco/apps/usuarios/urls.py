from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth

from . import views

app_name = 'usuarios'
urlpatterns = [
    path('login/', auth.LoginView.as_view(template_name='usuarios\login.html'),name='login'),
    path('register/',views.Register, name="register"),
    path('logout/', auth.LogoutView.as_view(), name = 'logout'),
]
