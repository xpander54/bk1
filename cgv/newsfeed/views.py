# -*- ecoding: utf-8 -*-

import string
import random

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404

from newsfeed.models import Subscriptor, Feed
from newsfeed.forms import EmailNewsfeedForm, EmailForm

#Mover esto a otro lado (parche temporal)
from blog.models import Post


# Movel a views.py en cursos >
def index(request):

	if request.method == 'POST':

		forma_subscripcion = EmailNewsfeedForm(request.POST)

		if forma_subscripcion.is_valid():

			subscriptor = forma_subscripcion.save(commit = False)
			subscriptor.feed = Feed.objects.get(pk = 2)
			# PASAR ESTO AL MODELO >
			subscriptor.codigo = __generate_code()
			# PASAR ESTO AL MODELO <

			email_subject = "Confrimación subscripción Neewsfeed CGV"
			email_message = """
				Para confirmar su subscripción al neewsfeed visite el siguiente liga:

				http://localhost:8000/%s/newsfeed-confirm/
			""" % subscriptor.codigo
			email_to     = subscriptor.email

			if __send_email(email_subject, email_message, email_to):

				subscriptor.save()
				return HttpResponseRedirect('/')
				
			else:
				return HttpResponse('Errores!!!')


	else:
		forma_subscripcion = EmailNewsfeedForm()
		

	reflexiones = Post.objects.filter(estado = 'p', destacado = True, categoria__nombre = 'reflexiones')
	video       = reflexiones.filter(tags__nombre = 'video')
	audio       = reflexiones.filter(tags__nombre = 'audio')
	ebook       = reflexiones.filter(tags__nombre = 'ebook')
	testimonios = Post.objects.filter(categoria__nombre = 'testimonios')

	context = {
		# Esto hay que moverlo!!!!
		'forma_subscripcion' : forma_subscripcion,
		'video'              : video,
		'audio'              : audio,
		'ebook'              : ebook,
		'testimonios'        : testimonios,
	}
	
	return render(request, 'newsfeed/index.html', context)
# Movel a views.py en cursos <


def newsfeed_confirm(request, code):

	subscriptor = get_object_or_404(Subscriptor, codigo = code)

	if subscriptor.activo == False:

		subscriptor.activo = True
		subscriptor.save()

		return HttpResponse('Correo Confirmado.')

	return HttpResponse('El correo ya había sido confirmado.')


def newsfeed_deactivate(request, code):
	subscriptor = get_object_or_404(Subscriptor, codigo = code)

	if subscriptor.activo == True:

		subscriptor.activo = False
		subscriptor.save()

		return HttpResponse('Subscripción desactivada.')

	return HttpResponse('la subscripción ya había sido cancelada.')

def newsfeed_send_code(request):

	if request.method == 'POST':

		forma = EmailForm(request.POST)

		if forma.is_valid():

			correo = forma.cleaned_data['email']

			try:

				subscriptor   = Subscriptor.objects.get(email = correo)
				email_subject = "Envío de código para desactivar newsfeed CGV"
				email_message = """
					http://localhost:8000/%s/newsfeed-deactivate/
				""" % subscriptor.codigo

				if __send_email(email_subject, email_message, correo):

					return HttpResponse('Sé ha enviado el código de desactivación a su cuenta de correo electrónico')


			except Subscriptor.DoesNotExist:

				return HttpResponse('El correo electrónico no coincide con ningun subscriptor.')

			# return HttpResponse(correo)

	else:
		forma = EmailForm()


	context = {
		'forma_codigo' : forma,
	}

	return render(request, 'newsfeed/send_code.html', context)


# PASAR ESTO AL MODELO >
def __generate_code(size = 10, chars = string.ascii_uppercase + string.ascii_lowercase + string.digits):

		return ''.join(random.choice(chars) for x in range(size))
# PASAR ESTO AL MODELO <

def __send_email(subject, message, to):

	try:
		send_mail(subject, message, to, ['netorcido@gmail.com'], fail_silently = False)

		return True

	except BadHeaderError:

		return False
	
