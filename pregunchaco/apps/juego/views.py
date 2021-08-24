from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PyR
import random
from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.

@login_required
def juego(request):
	context = {} 
	fila_pregunta = models.PyR.objects.get(id = 1) 
	context['preguntas'] = fila_pregunta

	if request.method=='POST' and fila_pregunta.respuesta in request.POST:

		return redirect('usuarios:login')

	else:
		pass


	return render(request,'juego/Game.html',context)


#if request.method=='POST' and 'btnform1' in request.POST:


