from django.shortcuts import render
from django.contrib.auth.decorators import login_required
"""
from django.contrib.auth.forms import UserCreationForm

def Registro(request):
	form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save(commit=False)
	
	context = {}
"""
def Main(request):
	return render(request, 'Main.html')

def Register(request):
	return render(request, 'Register.html')

@login_required
def Game(request):
	return render(request, 'Game.html')

@login_required
def Index(request):
	return render(request, 'Index.html')

@login_required
def Statistic(request):
	return render(request, 'Statistic.html')

