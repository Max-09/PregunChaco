from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages

# Create your views here.

def Register(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f' {username} pudo registrarse correctamente')
            return redirect('usuarios:login')

    else:
        form = forms.UserRegisterForm()
    
    context = {'form': form}
	
    return render(request, 'usuarios\Register.html', context)