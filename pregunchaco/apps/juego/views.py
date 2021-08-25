from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PyR
import random
from django.shortcuts import render, redirect
from . import forms
from . import models
from apps.usuarios.models import Usuario

# Create your views here.
@login_required
def juego(request):
	

	if request.method=='POST' and "empezar" in request.POST:
		partida=models.Partida()
		current_user = request.user
		partida.id_usuario=current_user.id
		partida.save()
		request.session["id_partida"]=partida.id

		return redirect('juego:1')
	else:
		pass
	
	return render(request, 'juego/Informacion.html')


@login_required
def pregunta1(request):
	
	cantidad = models.PyR.objects.all().count() #CANTIDAD DE PREGUNTAS
	ids=[]
	for i in range(1, cantidad+1):
		posible=models.PyR.objects.get(id=i) #RECORRO TODAS LAS PREGUNTAS

		if posible.cat_id==1: #FILTRO LAS DE GEOGRAFIA
			ids.append(posible.id) #AGREGO LOS IDS DE LAS PREGUNTAS A LA LISTA
		
	eleccion=random.choice(ids) #ELIJO UN IDS RANDOM ENTRE LAS PREGUNTAS DE GEO
	
	context = {} 
	fila_pregunta = models.PyR.objects.get(id=eleccion) #LE DOY EL ID RANDOM
	context['preguntas'] = fila_pregunta

	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:
		id_partida=request.session.get("id_partida")
		partida=models.Partida.get(id = id_partida)
		partida.aciertos=partida.aciertos + 1
		partida.save()
		return redirect('juego:2')

	elif request.method=='POST':
		return redirect('juego:2')

	return render(request,'juego/Game.html',context)


def pregunta2(request):

	context = {} 
	fila_pregunta = models.PyR.objects.get(id = 2) 
	context['preguntas'] = fila_pregunta
	puntaje = 0
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:
		puntaje = puntaje + 1
		
	else:
		pass

	return render(request,'juego/Game.html',context)


def pregunta3(request):

	context = {} 
	fila_pregunta = models.PyR.objects.get(id = 1) 
	context['preguntas'] = fila_pregunta
	puntaje = 0
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:
		puntaje = puntaje + 1
		
		

	else:
		pass

	return render(request,'juego/Game.html',context)


def pregunta4(request):

	context = {} 
	fila_pregunta = models.PyR.objects.get(id = 1) 
	context['preguntas'] = fila_pregunta
	puntaje = 0
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:
		puntaje = puntaje + 1
		
		

	else:
		pass

	return render(request,'juego/Game.html',context)


def pregunta5(request):

	context = {} 
	fila_pregunta = models.PyR.objects.get(id = 1) 
	context['preguntas'] = fila_pregunta
	puntaje = 0
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:
		puntaje = puntaje + 1
		
		

	else:
		pass

	return render(request,'juego/Game.html',context)


def pregunta6(request):

	context = {} 
	fila_pregunta = models.PyR.objects.get(id = 1) 
	context['preguntas'] = fila_pregunta
	puntaje = 0
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:
		puntaje = puntaje + 1
		
		

	else:
		pass

	return render(request,'juego/Game.html',context)


def pregunta7(request):

	context = {} 
	fila_pregunta = models.PyR.objects.get(id = 1) 
	context['preguntas'] = fila_pregunta
	puntaje = 0
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:
		puntaje = puntaje + 1
		
		

	else:
		pass

	return render(request,'juego/Game.html',context)




