from django import forms
from . import models

class formJuego(forms.ModelForm):
    class Meta:
        model = models.PyR
        fields = '__all__'
        #widgets = {forms.TextInput(attrs={'class': 'input-field', 'placeholder':'USUARIO', 'required':'required'}),}
                       
