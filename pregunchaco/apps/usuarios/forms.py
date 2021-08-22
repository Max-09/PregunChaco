from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #contraseña1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    #contraseña2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = models.Usuario
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k:"" for k in fields}
