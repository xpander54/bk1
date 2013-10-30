# -*- ecoding: utf-8 -*-

import string
import random

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404

from newsfeed.models import Subscriptor, Feed
from newsfeed.forms import EmailNewsfeedForm

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
		forma_subscripcion = IndexFeedForm()
		

	context = {
		'forma_subscripcion' : forma_subscripcion, 
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
	susbscriptor = get_object_or_404(Subscriptor, codigo = code)

	if subscriptor.activo == True:

		subscriptor.activo = False
		subscriptor.save()

		return HttpResponse('Subscripción desactivada.')

	return HttpResponse('la subscripción ya había sido cancelada.')

def newsfeed_send_code(request):

	return HttpResponse('Sección en Construcción')


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
	
