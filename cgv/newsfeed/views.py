# -*- ecoding: utf-8 -*-

import string
import random

from django.core.mail import send_mail, BadHeaderError

from django.core.mail import EmailMultiAlternatives

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



			email_subject = "Bienvenido y gracias por tu interes en pertenecer a nuestro newsletter."
			email_message = """
				En Gaby Valdes respetamos tu privacidad y tus datos están protegidos.
				Da click en la liga siguiente y recibe consejos, videos, audios y promociones.

				http://gabyvaldes.com/%s/newsfeed-confirm/
			""" % suscriptor.codigo
			email_to     = suscriptor.email

			

			
			
			if __send_email(email_subject, email_message, email_to):

				suscriptor.save()

				#return HttpResponseRedirect('/')
				return HttpResponse('Gracias. Revisa tu correo electrónico y confirma tu suscripción. (no olvides revisar el correo no deseado) <a href="http://www.gabyvaldes.com">regresar</a>')
				
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

		email_to     = suscriptor.email

		subject, from_email, to = 'Bienvenido a Gaby Valdes Newsletter', 'from@example.com', [email_to]
		text_content = 'Bienvenido a Gaby Valdes, para leer este correo, necesitas un lector que soporte HTML'
		html_content = '<p>Gracias por permitirme ser parte de tu comunidad!</p><p>Te doy la bienvenida a este sitio donde podremos compartir infinidad de temas de inter&eacute;s, estoy aqu&iacute; para entender y atender tus inquietudes, para que podamos juntos encontrar mejores maneras de relacionarnos con los dem&aacute;s y con nosotros mismos. S&eacute; que hay muchas cosas importantes en tu vida, y que parecer&iacute;a que el tiempo se hace mas corto y el mundo mas peque&ntilde;o, por lo que a veces puedes sentirte confundido en temas vitales: pareja, hijos, dinero, &eacute;xito, trabajo, espiritualidad, salud, superaci&oacute;n personal&#8230;por eso estoy aqu&iacute;, contigo y para ti, para escuchar tus necesidades y brindarte las herramientas adecuadas. Ahora que eres parte de esta comunidad vas a recibir semanalmente informaci&oacute;n y herramientas muy &uacute;tiles, por lo que te sugiero que dediques unos minutos a revisar el material que recibir&aacute;s.</p><p>Mi inter&eacute;s es darte sugerencias f&aacute;ciles, que no te quiten mucho tiempo, por lo que encontraras contenido claro y conciso. Si&eacute;ntete libre de compartir la informaci&oacute;n que aqu&iacute; recibes de manera gratuita, y por favor deja tus comentarios, ya que el material que se env&iacute;a esta basado en los intereses de la propia comunidad. &iquest;Cuales son tus gustos? &iquest;Que temas te apasionan? &iquest;Que quieres aprender? Estoy segura que siempre es un buen momento para estar mejor y disfrutar de la vida, mas all&aacute; de las complicaciones del momento, y s&eacute; que si est&aacute;s aqu&iacute; conmigo es porque tienes ganas de encontrar mayor plenitud y armon&iacute;a.</p><p>Felicidades!! Estoy convencida de que las casualidades no existen, si nos hemos encontrado en este momento ser&aacute;, seguramente para algo constructivo, y deseo que esta relaci&oacute;n que hoy iniciamos sea muy fruct&iacute;fera y llena de satisfacciones. Un abrazo donde quiera que est&eacute;s, estamos en contacto permanente, y, de nuevo,</p><p>BIENVENIDO!!</p><p>Gaby Vald&eacute;s</p><p><a href="http://www.gabyvaldes.com">www.gabyvaldes.com</a></p><p><a href="mailto:contacto@gabyvaldes.com">contacto@gabyvaldes.com</a></p><p><img src="http://cursos.gabyvaldes.com/wp-content/uploads/2014/03/logo-login.png" /></p>'
		msg = EmailMultiAlternatives(subject, text_content, from_email, [email_to])
		msg.attach_alternative(html_content, "text/html")
		msg.send()

		return HttpResponse('Correo Confirmado. <a href="http://www.gabyvaldes.com">regresar</a>')

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
		send_mail(subject, message, to, [to], fail_silently = False)

		return True

	except BadHeaderError:

		return False
	
