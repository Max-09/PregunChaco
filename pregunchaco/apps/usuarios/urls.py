from django.contrib import admin
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth
from . import views
from apps.usuarios import forms

app_name = 'usuarios'
urlpatterns = [
    path('login/', auth.LoginView.as_view(template_name='usuarios\login.html'),name='login'),
    path('register/',views.Register, name="register"),
    path('logout/', auth.LogoutView.as_view(), name = 'logout'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('recuperarcontrasena/', auth.PasswordResetView.as_view(success_url=reverse_lazy('usuarios:password_reset_done'),
    template_name=r'usuarios/recuperarcontrasena.html',
    form_class=forms.CaptchaPasswordResetForm,
    email_template_name = r'usuarios/correocontra.html'
    ), 
    name='recuperar'),
    path('reset_password_sent/', auth.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('recuperarcontrasena/<uidb64>/<token>/', auth.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('usuarios:password_reset_complete'),
        #form_class = forms.CaptchaPasswordResetChangeForm,
        #template_name = 'usuarios/cambiarcontrasena.html'
        ),
        name='password_reset_confirm'),
    path('reset_password_complete/', auth.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]
