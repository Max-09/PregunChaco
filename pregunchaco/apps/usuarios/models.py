from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
	maximo = models.IntegerField(default = 0)
	def __str__(self):
		return self.maximo