from django.contrib import admin
from django.urls import path


from . import views
from . import viewsstats
app_name = 'juego'

urlpatterns = [
    path('juego/', views.juego, name='juego'),
    path('juego/1', views.pregunta1 ,name='1'),
    path('juego/2', views.pregunta2 ,name='2'),
    path('juego/3', views.pregunta3 ,name='3'),
    path('juego/4', views.pregunta4 ,name='4'),
    path('juego/5', views.pregunta5 ,name='5'),
    path('juego/6', views.pregunta6 ,name='6'),
    path('juego/7', views.pregunta7 ,name='7'),
    path('juego/resultado', viewsstats.Resultado ,name='resultado'),
    path('juego/mis_estadisticas', viewsstats.mi_estadistica ,name='misestadisticas'),
    path('juego/elegircategoria', views.elegircategoria, name='elegircategoria'),
]
    