from django.db import models
from apps.usuarios.models import Usuario
# Create your models here.

class Categoria(models.Model):
	nombre = models.CharField(max_length = 50)

	def __str__(self):
		return self.nombre

class Modalidad(models.Model):
	nombrer = models.CharField(max_length = 50)


class PyR(models.Model):
	pregunta = models.CharField(max_length = 150)
	op1 = models.CharField(max_length = 150)
	op2 = models.CharField(max_length = 150)
	op3 = models.CharField(max_length = 150)
	op4 = models.CharField(max_length = 150)
	respuesta = models.CharField(max_length = 150)
	cat = models.ForeignKey(Categoria, on_delete = models.SET_NULL , null = True)

	def __str__(self):
		return self.pregunta

	def ObtenerPregunta(self):
		objeto = self.PyR.objects.get(id = 1)
		return objeto

class Partida(models.Model):
	id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null = True)
	modalidad = models.ForeignKey(Modalidad, on_delete = models.SET_NULL, null = True)
	acierto_1 = models.IntegerField(default = 0)
	acierto_2 = models.IntegerField(default = 0)
	acierto_3 = models.IntegerField(default = 0)
	acierto_4 = models.IntegerField(default = 0)
	acierto_5 = models.IntegerField(default = 0)
	acierto_6 = models.IntegerField(default = 0)
	acierto_7 = models.IntegerField(default = 0)


	
