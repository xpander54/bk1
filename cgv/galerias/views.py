from django.shortcuts import render
from galerias.models import Galeria, Imagen


def galerias(request):

	galerias = Galeria.objects.all()
	imagenes = Imagen.objects.all()

	context = {
		'galerias'  : galerias,
		'imagenes' : imagenes,
	}

	return render(request, 'galerias/tinymce.html', context)