from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.usuarios.models import Usuario
"""
from django.contrib.auth.forms import UserCreationForm

def Registro(request):
	form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save(commit=False)
	
	context = {}
"""
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
	list(lista[0:6])
	flat_lista = []
	for sublist in lista:
		for item in sublist:
				flat_lista.append(item)
	flat_lista[0] = flat_lista[0].upper()
	flat_lista[2] = flat_lista[2].upper()
	flat_lista[4] = flat_lista[4].upper()
	context['ranking'] = flat_lista[0:6]
	#Employer.objects.values('id').annotate(jobtitle_count=Count('jobtitle')).order_by('-jobtitle_count')[:5]
	return render(request,'top_estadistica.html', context)
		



