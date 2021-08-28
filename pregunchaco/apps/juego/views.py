import random



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import render, redirect
from django.contrib import messages

from . import models

def conseguir_pregunta_mixtas(cat_id):
	cantidad = models.PyR.objects.all().count() #CANTIDAD DE PREGUNTAS
	ids=[]
	for i in range(1, cantidad+1):
		posible=models.PyR.objects.get(id=i) #RECORRO TODAS LAS PREGUNTAS

		if posible.cat_id==cat_id: #FILTRO LAS DE GEOGRAFIA
			ids.append(posible.id) #AGREGO LOS IDS DE LAS PREGUNTAS A LA LISTA
	global eleccion		
	eleccion=random.choice(ids) #ELIJO UN IDS RANDOM ENTRE LAS PREGUNTAS DE GEO
	
	return eleccion

def conseguir_pregunta_categoria(cat_id):
	totalpreguntas = models.PyR.objects.filter(cat_id=cat_id).values_list("id") #CANTIDAD DE PREGUNTAS
	totalpreguntas = list(totalpreguntas)
	random.shuffle(totalpreguntas)

	global flat_ids
	ids=[]
	for i in range(7):
		ids.append(totalpreguntas.pop(0)) #AGREGO LOS IDS DE LAS PREGUNTAS A LA LISTA

	flat_ids = []
	for sublist in ids:
		for item in sublist:
			flat_ids.append(item)

	return flat_ids

def actualizar_puntaje(request):
	id_partida = request.session.get('id_partida') # consigo el id de la partida en juego
	partida = models.Partida.objects.get(id=id_partida) # pido a la BD la partida
	partida.aciertos = F('aciertos')+1 # sumo un punto a columna acierto
	partida.save() # guardo en BD


# Create your views here.
@login_required
def juego(request):
		
	if request.method=='POST' and "empezar" in request.POST:
		lista_preguntas= []
		for i in range(1, 8):
			conseguir_pregunta_mixtas(i)
			lista_preguntas.append(eleccion)
		partida=models.Partida()
		request.session["lista"] = lista_preguntas
		partida.id_usuario=request.user
		partida.save()
		request.session["id_partida"]=partida.id #GUARDO ID DE LA PARTIDA
		request.session["qcontestadas"] = 0
		return redirect('juego:1')
	elif request.method=='POST' and "categoria" in request.POST:
		return redirect('juego:elegircategoria')
	else:
		pass
	
	return render(request, 'juego/Informacion.html')

@login_required
def elegircategoria(request):
	if request.method=='POST':
	
		if "1" in request.POST:
			conseguir_pregunta_categoria(1)
		
		elif "2" in request.POST:
			conseguir_pregunta_categoria(2)
		
		elif "3" in request.POST:
			conseguir_pregunta_categoria(3)
		
		elif "4" in request.POST:
			conseguir_pregunta_categoria(4)
			
		elif "5" in request.POST:
			conseguir_pregunta_categoria(5)
		
		elif "6" in request.POST:
			conseguir_pregunta_categoria(6)
			
		elif "7" in request.POST:
			conseguir_pregunta_categoria(7)
		
		partida=models.Partida()
		request.session["lista"] = flat_ids
		partida.id_usuario=request.user
		partida.save()
		request.session["id_partida"]=partida.id #GUARDO ID DE LA PARTIDA
		request.session["qcontestadas"] = 0
		return redirect('juego:1')
	
	else:
		pass
	
	return render(request, 'juego/elegircategoria.html')

def traer_pregunta(request):
	global context, lista_preguntas, fila_pregunta
	context = {} 
	lista_preguntas = request.session.get("lista")

	try:
		fila_pregunta = models.PyR.objects.get(id=lista_preguntas[0])
		opciones = [fila_pregunta.op1, fila_pregunta.op2, fila_pregunta.op3, fila_pregunta.op4]
		random.shuffle(opciones)
		context['preguntas'] = fila_pregunta
		context['opcion1'] = opciones[0]
		context['opcion2'] = opciones[1]
		context['opcion3'] = opciones[2]
		context['opcion4'] = opciones[3]
		return context, request, lista_preguntas, fila_pregunta
		
	except:
		return redirect('juego:resultado')

def resultado_correcto(request):
	actualizar_puntaje(request)

	if request.session.get("qcontestadas") < 7:
		messages.success(request, message = ' LA RESPUESTA ANTERIOR FUE CORRECTA')

		request.session["qcontestadas"] += 1
		lista_preguntas.pop(0)
		request.session["lista"] = lista_preguntas


	else:
		return redirect('juego:resultado')

def resultado_incorrecto(request):
	if request.session["qcontestadas"] < 7:
		messages.error(request, message = 'LA RESPUESTA ANTERIOR FUE CORRECTA')
	
		request.session["qcontestadas"] += 1
		lista_preguntas.pop(0)
		request.session["lista"] = lista_preguntas

	else:
		return redirect('juego:resultado')

@login_required
def pregunta1(request):

	traer_pregunta(request)

	if request.method=='POST' and fila_pregunta.respuesta in request.POST: #SI RESPONDIO BIEN, ENTRA
		resultado_correcto(request)
		return redirect('juego:2')
	elif request.method=='POST':
		resultado_incorrecto(request)
		return redirect('juego:2')
	
	return render(request,'juego/Game.html',context)

@login_required
def pregunta2(request):

	traer_pregunta(request)

	if request.method=='POST' and fila_pregunta.respuesta in request.POST: #SI RESPONDIO BIEN, ENTRA
		resultado_correcto(request)
		return redirect('juego:3')
	
	elif request.method=='POST':
		resultado_incorrecto(request)
		return redirect('juego:3')

	return render(request,'juego/Game.html',context)

@login_required
def pregunta3(request):

	traer_pregunta(request)

	if request.method=='POST' and fila_pregunta.respuesta in request.POST: #SI RESPONDIO BIEN, ENTRA
		resultado_correcto(request)
		return redirect('juego:4')
	
	elif request.method=='POST':
		resultado_incorrecto(request)
		return redirect('juego:4')
	
	return render(request,'juego/Game.html',context)

@login_required
def pregunta4(request):

	traer_pregunta(request)
	if request.method=='POST' and fila_pregunta.respuesta in request.POST: #SI RESPONDIO BIEN, ENTRA
		resultado_correcto(request)
		return redirect('juego:5')
	
	elif request.method=='POST':
		resultado_incorrecto(request)
		return redirect('juego:5')

	return render(request,'juego/Game.html',context)

@login_required
def pregunta5(request):

	traer_pregunta(request)
	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST: #SI RESPONDIO BIEN, ENTRA
		resultado_correcto(request)
		return redirect('juego:6')
	
	elif request.method=='POST':
		resultado_incorrecto(request)
		return redirect('juego:6')

	return render(request,'juego/Game.html',context)

@login_required
def pregunta6(request):
	traer_pregunta(request)
	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST: #SI RESPONDIO BIEN, ENTRA
		resultado_correcto(request)
		return redirect('juego:7')
	
	elif request.method=='POST':
		resultado_incorrecto(request)
		return redirect('juego:7')

	return render(request,'juego/Game.html',context)

@login_required
def pregunta7(request):

	traer_pregunta(request)
	
	if request.method=='POST' and fila_pregunta.respuesta in request.POST: #SI RESPONDIO BIEN, ENTRA
		resultado_correcto(request)
		return redirect('juego:resultado')
	
	elif request.method=='POST':
		resultado_incorrecto(request)
		return redirect('juego:resultado')

	return render(request,'juego/Game.html',context)

