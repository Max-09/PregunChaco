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
    puntaje = int((partida.aciertos)*14.29)
    errores = abs(7- partida.aciertos)	
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
    

    return render(request,'juego/misestadisticas.html', context)

