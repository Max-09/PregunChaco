import random

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import render, redirect

from . import models


def conseguir_pregunta(cat_id):
	cantidad = models.PyR.objects.all().count() #CANTIDAD DE PREGUNTAS
	ids=[]
	for i in range(1, cantidad+1):
		posible=models.PyR.objects.get(id=i) #RECORRO TODAS LAS PREGUNTAS

		if posible.cat_id==cat_id: #FILTRO LAS DE GEOGRAFIA
			ids.append(posible.id) #AGREGO LOS IDS DE LAS PREGUNTAS A LA LISTA
	global eleccion		
	eleccion=random.choice(ids) #ELIJO UN IDS RANDOM ENTRE LAS PREGUNTAS DE GEO
	
	return eleccion

def actualizar_puntaje(request):
	id_partida = request.session.get('id_partida') # consigo el id de la partida en juego
	partida = models.Partida.objects.get(id=id_partida) # pido a la BD la partida
	partida.aciertos = F('aciertos')+1 # sumo un punto a columna acierto
	partida.save() # guardo en BD



# Create your views here.
@login_required
def juego(request):
	#NO SE TIENE QUE GUARDAR EN LA BDD PARTIDA, YA QUE CREA VARIAS IDS DE PARTIDA EN LA MISMA PARTIDA, COMO SI JUGAS VARIAS PARTIDAS EN LA MISMA
	
	if request.method=='POST' and "empezar" in request.POST:
		lista_preguntas= []
		for i in range(1, 8):
			conseguir_pregunta(i)
			lista_preguntas.append(eleccion)
		partida=models.Partida()
		request.session["lista"] = lista_preguntas
		request.session["aciertos"] = 0
		request.session["prueba"] = "prueba"
		partida.id_usuario=request.user
		partida.aciertos=request.session.get("aciertos")
		partida.save()
		request.session["id_partida"]=partida.id #GUARDO ID DE LA PARTIDA
		return redirect('juego:1')
	else:
		pass
	
	return render(request, 'juego/Informacion.html')


@login_required
def pregunta1(request):

	context = {} 
	lista_preguntas = request.session.get("lista")
	try:
		fila_pregunta = models.PyR.objects.get(id=lista_preguntas[0]) 
		context['preguntas'] = fila_pregunta
	except:
		return redirect('juego:estadistica')


	if request.method=='POST' and fila_pregunta.respuesta in request.POST: #SI RESPONDIO BIEN, ENTRA
		
		actualizar_puntaje(request)
		lista_preguntas.pop(0)
		request.session["lista"] = lista_preguntas
		return redirect('juego:2')

	elif request.method=='POST':
		lista_preguntas.pop(0)
		request.session["lista"] = lista_preguntas
		return redirect('juego:2')
		
	return render(request,'juego/Game.html',context)


def pregunta2(request):

	context = {} 
	lista_preguntas = request.session.get("lista")
	try:
		fila_pregunta = models.PyR.objects.get(id=lista_preguntas[0]) 
		context['preguntas'] = fila_pregunta
	except:
		return redirect('juego:estadistica')

	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:

		actualizar_puntaje(request)
		lista_preguntas.pop(0)
		request.session["lista"] = lista_preguntas
		return redirect('juego:3')


	elif request.method=='POST':
		lista_preguntas.pop(0)
		request.session["lista"] = lista_preguntas
		return redirect('juego:3')

	return render(request,'juego/Game.html',context)

def pregunta3(request):

	context = {} 
	lista_preguntas = request.session.get("lista")
	try:
		fila_pregunta = models.PyR.objects.get(id=lista_preguntas[0]) 
		context['preguntas'] = fila_pregunta
	except:
		return redirect('juego:estadistica')

	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:

		actualizar_puntaje(request)
		lista_preguntas.pop(0)
		request.session["lista"] = lista_preguntas
		return redirect('juego:4')
		
	elif request.method=='POST':

		lista_preguntas.pop(0)
		request.session["lista"] = lista_preguntas
		return redirect('juego:4')
		

	return render(request,'juego/Game.html',context)

def pregunta4(request):

	context = {} 
	lista_preguntas = request.session.get("lista")
	try:
		fila_pregunta = models.PyR.objects.get(id=lista_preguntas[0]) 
		context['preguntas'] = fila_pregunta
	except:
		return redirect('juego:estadistica')
	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:

		actualizar_puntaje(request)
		lista_preguntas.pop(0)
		request.session["lista"] = lista_preguntas
		return redirect('juego:5')
		

	elif request.method=='POST':
		lista_preguntas.pop(0)
		request.session["lista"] = lista_preguntas
		return redirect('juego:5')

	return render(request,'juego/Game.html',context)

def pregunta5(request):

	context = {} 
	lista_preguntas = request.session.get("lista")
	try:
		fila_pregunta = models.PyR.objects.get(id=lista_preguntas[0]) 
		context['preguntas'] = fila_pregunta
	except:
		return redirect('juego:estadistica')

	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:

		actualizar_puntaje(request)
		lista_preguntas.pop(0)
		request.session["lista"] = lista_preguntas
		return redirect('juego:6')


	elif request.method=='POST':
		lista_preguntas.pop(0)
		request.session["lista"] = lista_preguntas
		return redirect('juego:6')

	return render(request,'juego/Game.html',context)

def pregunta6(request):

	context = {} 
	lista_preguntas = request.session.get("lista")
	try:
		fila_pregunta = models.PyR.objects.get(id=lista_preguntas[0]) 
		context['preguntas'] = fila_pregunta
	except:
		return redirect('juego:estadistica')
	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:

		actualizar_puntaje(request)
		lista_preguntas.pop(0)
		request.session["lista"] = lista_preguntas
		return redirect('juego:7')


	elif request.method=='POST':
		lista_preguntas.pop(0)
		request.session["lista"] = lista_preguntas
		return redirect('juego:7')

	return render(request,'juego/Game.html',context)

def pregunta7(request):

	context = {} 
	lista_preguntas = request.session.get("lista")
	try:
		fila_pregunta = models.PyR.objects.get(id=lista_preguntas[0]) 
		context['preguntas'] = fila_pregunta
	except:
		return redirect('juego:estadistica')

	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:
		
		actualizar_puntaje(request)
		lista_preguntas.pop(0)
		request.session["lista"] = lista_preguntas
		return redirect('juego:estadistica')
	elif request.method=='POST':
		lista_preguntas.pop(0)
		request.session["lista"] = lista_preguntas
		return redirect('juego:estadistica')

	return render(request,'juego/Game.html',context)

def Resultado(request):
	return render(request, 'juego/Statistic.html')