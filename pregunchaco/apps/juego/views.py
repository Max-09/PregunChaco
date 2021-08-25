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
	#NO SE TIENE QUE GUARDAR EN LA BDD PARTIDA, YA QUE CREA VARIAS IDS DE PARTIDA EN LA MISMA PARTIDA, COMO SI JUGAS VARIAS PARTIDAS EN LA MISMA

	if request.method=='POST' and "empezar" in request.POST:
		partida=models.Partida()
		request.session["id_partida"]=partida.id #GUARDO ID DE LA PARTIDA
		request.session["aciertos"] = 0
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

		if posible.cat_id=="1": #FILTRO LAS DE GEOGRAFIA
			ids.append(posible.id) #AGREGO LOS IDS DE LAS PREGUNTAS A LA LISTA
			
	print(ids)	
	eleccion=random.choice(ids) #ELIJO UN IDS RANDOM ENTRE LAS PREGUNTAS DE GEO
	
	context = {} 
	fila_pregunta = models.PyR.objects.get(id=eleccion) #LE DOY EL ID RANDOM
	context['preguntas'] = fila_pregunta

	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST: #SI RESPONDIO BIEN, ENTRA
		print(request.session.get("id_partida")) #SOLO DE PRUEBA, NO HACE NA
		
		request.session["aciertos"] = 1 #GUARDO EN VARIABLE DE SESION LOS ACIERTOS, PARA GUARDAR EN BASE DE DATOS AL FINAL
		
		return redirect('juego:2')

	elif request.method=='POST':

		return redirect('juego:2')

	return render(request,'juego/Game.html',context)


def pregunta2(request):

	cantidad = models.PyR.objects.all().count() #CANTIDAD DE PREGUNTAS
	ids=[]
	for i in range(1, cantidad+1):
		posible=models.PyR.objects.get(id=i) #RECORRO TODAS LAS PREGUNTAS

		if posible.cat_id=="2": 
			ids.append(posible.id) #AGREGO LOS IDS DE LAS PREGUNTAS A LA LISTA
		
	eleccion=random.choice(ids) #ELIJO UN IDS RANDOM ENTRE LAS PREGUNTAS DE GEO
	
	context = {} 
	fila_pregunta = models.PyR.objects.get(id=eleccion) #LE DOY EL ID RANDOM
	context['preguntas'] = fila_pregunta

	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:
		
		
		request.session["aciertos"] = 2
		
		return redirect('juego:3')

	elif request.method=='POST':

		return redirect('juego:3')

	return render(request,'juego/Game.html',context)

def pregunta3(request):

	cantidad = models.PyR.objects.all().count() #CANTIDAD DE PREGUNTAS
	ids=[]
	for i in range(1, cantidad+1):
		posible=models.PyR.objects.get(id=i) #RECORRO TODAS LAS PREGUNTAS

		if posible.cat_id=="3": 
			ids.append(posible.id) 
		
	eleccion=random.choice(ids)
	
	context = {} 
	fila_pregunta = models.PyR.objects.get(id=eleccion) 
	context['preguntas'] = fila_pregunta

	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:
		
		request.session["aciertos"] = 3
		return redirect('juego:4')
		
	elif request.method=='POST':
		return redirect('juego:4')

	return render(request,'juego/Game.html',context)

def pregunta4(request):

	cantidad = models.PyR.objects.all().count() #CANTIDAD DE PREGUNTAS
	ids=[]
	for i in range(1, cantidad+1):
		posible=models.PyR.objects.get(id=i) #RECORRO TODAS LAS PREGUNTAS

		if posible.cat_id=="4": 
			ids.append(posible.id) 
		
	eleccion=random.choice(ids)
	
	context = {} 
	fila_pregunta = models.PyR.objects.get(id=eleccion) 
	context['preguntas'] = fila_pregunta

	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:
		
		request.session["aciertos"] = 4
		return redirect('juego:5')
		

	elif request.method=='POST':
		return redirect('juego:5')

	return render(request,'juego/Game.html',context)

def pregunta5(request):

	cantidad = models.PyR.objects.all().count() #CANTIDAD DE PREGUNTAS
	ids=[]
	for i in range(1, cantidad+1):
		posible=models.PyR.objects.get(id=i) #RECORRO TODAS LAS PREGUNTAS

		if posible.cat_id=="5": 
			ids.append(posible.id) 
		
	eleccion=random.choice(ids)
	
	context = {} 
	fila_pregunta = models.PyR.objects.get(id=eleccion) 
	context['preguntas'] = fila_pregunta

	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:
		
		request.session["aciertos"] = 5
		return redirect('juego:6')


	elif request.method=='POST':
		return redirect('juego:6')

	return render(request,'juego/Game.html',context)

def pregunta6(request):

	cantidad = models.PyR.objects.all().count() #CANTIDAD DE PREGUNTAS
	ids=[]
	for i in range(1, cantidad+1):
		posible=models.PyR.objects.get(id=i) #RECORRO TODAS LAS PREGUNTAS

		if posible.cat_id=="6": 
			ids.append(posible.id) 
		
	eleccion=random.choice(ids)
	
	context = {} 
	fila_pregunta = models.PyR.objects.get(id=eleccion) 
	context['preguntas'] = fila_pregunta

	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:
		
		request.session["aciertos"] = 6
		return redirect('juego:7')


	elif request.method=='POST':
		return redirect('juego:7')

	return render(request,'juego/Game.html',context)

def pregunta7(request):

	cantidad = models.PyR.objects.all().count() 
	ids=[]
	for i in range(1, cantidad+1):
		posible=models.PyR.objects.get(id=i)

		if posible.cat_id=="7": 
			ids.append(posible.id)
	
	eleccion=random.choice(ids) 
	
	context = {} 
	fila_pregunta = models.PyR.objects.get(id=eleccion) 
	context['preguntas'] = fila_pregunta

	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:
		print(request.session.get("id_partida"))
		
		request.session["aciertos"] = 7
		partida=models.Partida()
		partida.id_usuario=request.user
		partida.aciertos=request.session.get("aciertos")
		partida.save()
		
		return redirect('juego:estadistica')
	elif request.method=='POST':

		partida=models.Partida()
		partida.id_usuario=request.user
		partida.aciertos=request.session.get("aciertos")
		partida.save()

		return redirect('juego:estadistica')

	return render(request,'juego/Game.html',context)

def Resultado(request):
	return render(request, 'juego/Statistic.html')