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


@login_required
def Index(request):
	return render(request, 'Index.html')



