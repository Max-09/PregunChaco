import math

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from apps.usuarios.models import Usuario
from django.db.models import Avg
from . import models

@login_required
def Resultado(request):
    context={}
    id_partida = request.session.get('id_partida') # consigo el id de la partida en juego
    partida = models.Partida.objects.get(id=id_partida) 
    aciertos = (partida.acierto_1 + partida.acierto_2 + partida.acierto_3 + partida.acierto_4 + partida.acierto_5 + partida.acierto_6 + partida.acierto_7)
    errores = abs(7- aciertos)	
    puntaje = int(aciertos*14.29)
    context['aciertos'] = aciertos
    context['puntaje']= puntaje
    context['errores'] = errores
    context['partida']= partida
    id_usuario = partida.id_usuario.id     
    usuario = Usuario.objects.get(id=id_usuario)    
    if usuario.maximo < puntaje:
        usuario.maximo = puntaje
        usuario.save()

    return render(request, 'juego/Statistic.html', context)

@login_required
def mi_estadistica(request):
    context={}
    usuario = request.user
    context['qpartidasjugadas'] = models.Partida.objects.filter(id_usuario=usuario).count()
    context['puntajemaximo'] = usuario.maximo
    promedio = models.Partida.objects.filter(id_usuario=usuario).values('aciertos').aggregate(Avg('aciertos'))

    context['puntajepromedio'] = int(promedio['aciertos__avg']*14.29)

    lista = list(Usuario.objects.all().order_by('-maximo'))
    
    indice = lista.index(request.user)+1
    context['indice'] = indice

    return render(request,'juego/misestadisticas.html', context)



