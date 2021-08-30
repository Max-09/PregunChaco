import pandas as pd

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from apps.usuarios.models import Usuario
from django.db.models import Avg
from . import models

@login_required
def Resultado(request):
    context={}
    context['contestadas'] = request.session.get('contestadas')
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
    categorias=["cultura_arte", "historia", "deporte", "geografia", "economia","ciencia","entretenimiento"]
    numcat=[1,2,3,4,5,6,7]
    numacierto=["acierto_1","acierto_2","acierto_3","acierto_4","acierto_5","acierto_6","acierto_7"]
    
    try:
        context={}
        usuario = request.user
        dataset =pd.DataFrame.from_records(models.Partida.objects.filter(id_usuario=usuario).values())
        cantidad = dataset["id"].count()
    except:
        return render(request, 'juego/noestadistica.html')
    
    promedio = dataset[["acierto_1", "acierto_2", "acierto_3", "acierto_4", "acierto_5", "acierto_6", "acierto_7"]].sum().sum()/(cantidad)

    context['qpartidasjugadas'] = cantidad
    context['puntajemaximo'] = usuario.maximo
    context['puntajepromedio'] = int(promedio*14.29)
    
    lista = list(Usuario.objects.all().order_by('-maximo'))
    indice = lista.index(request.user)+1
    context['indice'] = indice

    for i in range(7):
        categorias[i]={}
        qpreguntascontestadas = int((dataset[dataset["modalidad_id"].astype(int)==numcat[i]].count(axis=1).count())*7+(dataset[dataset["modalidad_id"].astype(int)==8].count(axis=1).count()))
        #cambiar " .astype(int) == 1" por id de categoria en linea anterior
        categorias[i]['qpreguntascontestadas'] = qpreguntascontestadas
        aciertos = int(dataset[[numacierto[i]]].sum().sum()) #cambiar "acierto_1" por acierto de categoria
        categorias[i]['aciertos']= aciertos
        try:
            promedio = int(aciertos/qpreguntascontestadas*100)
        except:
            promedio = 0
        categorias[i]['promedio']= promedio
        context[i] = categorias[i] #PROBLEMA ACA!!!!!!!
        

    return render(request,'juego/misestadisticas.html', context)



