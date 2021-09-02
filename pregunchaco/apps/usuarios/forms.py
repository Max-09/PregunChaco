from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import password_validation

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

class CaptchaPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class': 'input-field', 'placeholder':'CORREO', 'required':'required'}))
    class Meta:
        model = models.Usuario
        fields = ['email']
        help_text = {k:"" for k in fields}

class CaptchaPasswordResetChangeForm(SetPasswordForm):

    new_password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder':'CONTRASEÑA', 'required':'required'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label='Confirma Contraseña',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder':'REINGRESAR CONTRASEÑA', 'required':'required'}),
    )

  
    
    # password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder':'CONTRASEÑA', 'required':'required'}))
    # password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder':'REINGRESAR CONTRASEÑA', 'required':'required'}))
   
    # class Meta:
    #     model = models.Usuario
    #     fields = ['password1', 'password2']
    #     help_text = {k:"" for k in fields}