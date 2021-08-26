from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PyR
import random
from django.shortcuts import render, redirect
from . import forms
from . import models
from apps.usuarios.models import Usuario

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


# Create your views here.
@login_required
def juego(request):
	#NO SE TIENE QUE GUARDAR EN LA BDD PARTIDA, YA QUE CREA VARIAS IDS DE PARTIDA EN LA MISMA PARTIDA, COMO SI JUGAS VARIAS PARTIDAS EN LA MISMA

	if request.method=='POST' and "empezar" in request.POST:
		partida=models.Partida()
		request.session["id_partida"]=partida.id #GUARDO ID DE LA PARTIDA
		request.session["aciertos"] = 0
		request.session["prueba"] = "prueba"
		return redirect('juego:1')
	else:
		pass
	
	return render(request, 'juego/Informacion.html')


@login_required
def pregunta1(request):
	fila_pregunta = None
	if request.method=='POST' and fila_pregunta.respuesta in request.POST: #SI RESPONDIO BIEN, ENTRA
		print(fila_pregunta.respuesta)
		print(request.POST)
		print("contesta bien 1") #SOLO DE PRUEBA, NO HACE NA
		
		request.session["aciertos"] += 1 #GUARDO EN VARIABLE DE SESION LOS ACIERTOS, PARA GUARDAR EN BASE DE DATOS AL FINAL
		
		return redirect('juego:2')

	elif request.method=='POST':
		print(fila_pregunta.respuesta)
		print(request.POST)
		pass
		#return redirect('juego:2')

	conseguir_pregunta(1)
	print(request.session.get("prueba"))
	context = {} 
	fila_pregunta = models.PyR.objects.get(id=eleccion) #LE DOY EL ID RANDOM
	context['preguntas'] = fila_pregunta
	print(fila_pregunta.pregunta)

	return render(request,'juego/Game.html',context)


def pregunta2(request):

	conseguir_pregunta(2)
	print(request.session.get("prueba"))
	context = {} 
	fila_pregunta = models.PyR.objects.get(id=eleccion) 
	context['preguntas'] = fila_pregunta

	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:
		print("contesta bien 2")
		request.session["aciertos"] += 1
		return redirect('juego:3')


	elif request.method=='POST':
		pass
		# return redirect('juego:3')

	return render(request,'juego/Game.html',context)

def pregunta3(request):

	conseguir_pregunta(3)
	print(request.session.get("prueba"))
	context = {} 
	fila_pregunta = models.PyR.objects.get(id=eleccion) 
	context['preguntas'] = fila_pregunta

	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:
		print("contesta bien 3")
		request.session["aciertos"] += 1
		return redirect('juego:4')
		
	elif request.method=='POST':
		#return redirect('juego:4')
		pass

	return render(request,'juego/Game.html',context)

def pregunta4(request):

	conseguir_pregunta(4)
	print(request.session.get("prueba"))
	context = {} 
	fila_pregunta = models.PyR.objects.get(id=eleccion) 
	context['preguntas'] = fila_pregunta

	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:
		print("contesta bien 4")
		request.session["aciertos"] += 1
		return redirect('juego:5')
		

	elif request.method=='POST':
		pass
		#return redirect('juego:5')

	return render(request,'juego/Game.html',context)

def pregunta5(request):

	conseguir_pregunta(5)
	print(request.session.get("prueba"))
	context = {} 
	fila_pregunta = models.PyR.objects.get(id=eleccion) 
	context['preguntas'] = fila_pregunta

	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:
		print("contesta bien 5")
		request.session["aciertos"] += 1
		return redirect('juego:6')


	elif request.method=='POST':
		pass
		#return redirect('juego:6')

	return render(request,'juego/Game.html',context)

def pregunta6(request):

	conseguir_pregunta(6)
	print(request.session.get("prueba"))
	context = {} 
	fila_pregunta = models.PyR.objects.get(id=eleccion) 
	context['preguntas'] = fila_pregunta

	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:
		print("contesta bien 6")
		request.session["aciertos"] += 1
		return redirect('juego:7')


	elif request.method=='POST':
		pass
		#return redirect('juego:7')

	return render(request,'juego/Game.html',context)

def pregunta7(request):

	conseguir_pregunta(7)
	print(request.session.get("prueba"))
	context = {} 
	fila_pregunta = models.PyR.objects.get(id=eleccion) 
	context['preguntas'] = fila_pregunta

	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST:
		print("contesta bien 7")
		
		request.session["aciertos"] += 1
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