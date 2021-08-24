from django.db import models
#from .usuarios.models import Usuario
# Create your models here.

class Categoria(models.Model):
	nombre = models.CharField(max_length = 50)

	def __str__(self):
		return self.nombre

class PyR(models.Model):
	pregunta = models.CharField(max_length = 150)
	op1 = models.CharField(max_length = 150)
	op2 = models.CharField(max_length = 150)
	op3 = models.CharField(max_length = 150)
	op4 = models.CharField(max_length = 150)
	respuesta = models.CharField(max_length = 150)
	cat = models.ForeignKey(Categoria, on_delete = models.SET_NULL , null = True)

	def ObtenerPregunta(self):
		objeto = self.PyR.objects.get(id = 1)
		return objeto

#class Puntos(models.Model):
	#id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null = False)
	#aciertos = models.IntegerField(default = 0) 
