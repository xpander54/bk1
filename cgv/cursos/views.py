from django.shortcuts import render, get_object_or_404
from cursos.models import Curso
from django.http import HttpResponse, HttpResponseRedirect, Http404


def cursos(request):

	#forma_suscripcion = EmailNewsfeedForm()
	cursos       = Curso.objects.filter(estado = 'p')
	#abstract        = cursos.filter(tags__nombre = 'audio')
	#video             = cursos.filter(tags__nombre = 'video')
	#ebook             = cursos.filter(tags__nombre = 'ebook')
	context           = {
		'cursos'             : cursos,
		}


	return render(request, 'cursos/cursos.html', context)
