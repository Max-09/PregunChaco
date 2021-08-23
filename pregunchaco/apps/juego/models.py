from django.db import models

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
