from django.shortcuts import render
from newsfeed.models import Subscriptor
from newsfeed.forms import EmailNewsfeedForm

def contacto(request):
	return render(request, 'noticias/contacto.html')

def reflexiones(request):
	forma_mail = EmailNewsfeedForm()
	context = {
		'forma_suscripcion' : forma_mail,
	}    

	return render(request, 'noticias/reflexiones.html', context)