from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PyR

# Create your views here.

@login_required
def MostrarPreguntas(request):
	objeto = PyR.objects.get(id = 1)
	context = {} 
	context['preguntas'] = objeto 

	return render(request,'juego/Game.html',context)
