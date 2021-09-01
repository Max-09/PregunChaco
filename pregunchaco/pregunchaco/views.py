from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.usuarios.models import Usuario

def Main(request):
	return render(request, 'Main.html')

@login_required
def Index(request):
	context = {}
	context['user'] = request.user.username.upper()

	return render(request, 'Index.html', context)

def top_estadistica(request):
	context={}
	lista = Usuario.objects.all().order_by('-maximo').values_list('username', 'maximo')
	for i in range(6, -1, -2):
		try:
			lista = list(lista[0:i])
			flat_lista = []
			for sublist in lista:
				for item in sublist:
					flat_lista.append(item)
			for j in range(0,len(flat_lista), 2):
				print(j)
				flat_lista[j] = flat_lista[j].upper()
			break

		except:
			pass
	
	context['ranking'] = flat_lista
	return render(request,'top_estadistica.html', context)
		



