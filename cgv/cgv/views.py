from django.shortcuts import render
from newsfeed.forms import EmailNewsfeedForm
from django.http import HttpResponseRedirect, HttpResponse
from cgv.forms import ContactForm
from cgv.forms import LoginForm
from cgv.forms import RegistroForm



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
 

def login(request):
	login_form = LoginForm()
	context={
		'login_form' : login_form,
		}
	return render(request, 'login.html', context)

def registro(request):
	registro_form = RegistroForm()
	context={
		'registro_form' : registro_form,
		}
	return render(request, 'registro.html', context)

