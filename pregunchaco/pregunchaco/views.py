from django.shortcuts import render

def Main(request):
	return render(request, 'Main.html')

def Login(request):
	return render(request, 'Login.html')

def Game(request):
	return render(request, 'Game.html')