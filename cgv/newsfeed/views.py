# -*- ecoding: utf-8 -*-

import string
import random

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404

from newsfeed.models import Suscriptor, Feed
from newsfeed.forms import EmailNewsfeedForm, EmailForm

#Mover esto a otro lado (parche temporal)
from blog.models import Post


# Movel a views.py en cursos >
def index(request):

	if request.method == 'POST':

		forma_suscripcion = EmailNewsfeedForm(request.POST)

		if forma_suscripcion.is_valid():

			suscriptor = forma_suscripcion.save(commit = False)
			suscriptor.feed = Feed.objects.get(pk = 2)
			# PASAR ESTO AL MODELO >
			suscriptor.codigo = __generate_code()
			# PASAR ESTO AL MODELO <

			email_subject = "Confrimación subscripción Neewsfeed CGV"
			email_message = """
				Para confirmar su subscripción al neewsfeed visite la siguiente liga:

				http://gabyvaldes.com/%s/newsfeed-confirm/
			""" % suscriptor.codigo
			email_to     = suscriptor.email

			if __send_email(email_subject, email_message, email_to):

				suscriptor.save()
				return HttpResponseRedirect('/')
				
			else:
				return HttpResponse('Errores!!!')


	else:
		forma_suscripcion = EmailNewsfeedForm()
		

	reflexiones = Post.objects.filter(estado = 'p', destacado = True, categoria__nombre = 'reflexiones')
	video       = reflexiones.filter(tags__nombre = 'video')
	audio       = reflexiones.filter(tags__nombre = 'audio')
	ebook       = reflexiones.filter(tags__nombre = 'ebook')
	testimonios = Post.objects.filter(categoria__nombre = 'testimonios')

	context = {
		# Esto hay que moverlo!!!!
		'forma_suscripcion' : forma_suscripcion,
		'video'              : video,
		'audio'              : audio,
		'ebook'              : ebook,
		'testimonios'        : testimonios,
	}
	
	return render(request, 'newsfeed/index.html', context)
# Movel a views.py en cursos <


def newsfeed_confirm(request, code):

	suscriptor = get_object_or_404(Suscriptor, codigo = code)

	if suscriptor.activo == False:

		suscriptor.activo = True
		suscriptor.save()

		return HttpResponse('Correo Confirmado.')

	return HttpResponse('El correo ya había sido confirmado.')


def newsfeed_deactivate(request, code):
	suscriptor = get_object_or_404(Suscriptor, codigo = code)

	if suscriptor.activo == True:

		suscriptor.activo = False
		suscriptor.save()

		return HttpResponse('Subscripción desactivada.')

	return HttpResponse('la subscripción ya había sido cancelada.')

def newsfeed_send_code(request):

	if request.method == 'POST':

		forma = EmailForm(request.POST)

		if forma.is_valid():

			correo = forma.cleaned_data['email']

			try:

				suscriptor   = Suscriptor.objects.get(email = correo)
				email_subject = "Envío de código para desactivar newsfeed CGV"
				email_message = """
					http://gabyvaldes.com/%s/newsfeed-deactivate/
				""" % suscriptor.codigo

				if __send_email(email_subject, email_message, correo):

					return HttpResponse('Sé ha enviado el código de desactivación a su cuenta de correo electrónico')


			except Suscriptor.DoesNotExist:

				return HttpResponse('El correo electrónico no coincide con ningun suscriptor.')

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
		#send_mail(subject, message, to, ['rodrigo@holbox.bz'], fail_silently = False)
		send_mail(subject, message, to, [suscriptor.email], fail_silently = False)

		return True

	except BadHeaderError:

		return False
	
