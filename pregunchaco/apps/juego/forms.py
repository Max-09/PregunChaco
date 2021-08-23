from django import forms
from . import models

class formjuego(models.PyR):
    pregunta = forms.CharField(max_length = 150)
    op1 = forms.CharField(max_length = 150)
    op2 = forms.CharField(max_length = 150)
    op3 = forms.CharField(max_length = 150)
    op4 = forms.CharField(max_length = 150)
    respuesta = forms.CharField(max_length = 150)
    cat = forms.CharField(max_length = 50)
