from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

class UserRegisterForm(UserCreationForm):
    #username = forms.CharField(label='Usuario', widget=forms.CharField(attrs={'class': 'input-field', 'placeholder':'USUARIO', 'required':'required'}))
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class': 'input-field', 'placeholder':'CORREO', 'required':'required'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder':'CONTRASEÑA', 'required':'required'}))
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder':'REINGRESAR CONTRASEÑA', 'required':'required'}))
   
    class Meta:
        model = models.Usuario
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k:"" for k in fields}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-field', 'placeholder':'USUARIO', 'required':'required'}),
                        }
