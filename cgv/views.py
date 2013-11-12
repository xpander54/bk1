from django.shortcuts import render
from newsfeed.models import Subscriptor
from newsfeed.forms import EmailNewsfeedForm
from django.http import HttpResponseRedirect, HttpResponse
from cgv.forms import ContactForm

def contacto(request):
	return render(request, 'noticias/contacto.html')

def reflexiones(request):
	forma_mail = EmailNewsfeedForm()
	context = {
		'forma_suscripcion' : forma_mail,
	}    

	return render(request, 'noticias/reflexiones.html', context)

def contacto(request):

	if request.method == 'POST':
		forma_contacto = ContactForm(request.POST)

	else:
		forma_contacto = ContactForm()

	context={
		'forma_contacto' : forma_contacto,
	}

	return render(request, 'contacto.html', context)
    

