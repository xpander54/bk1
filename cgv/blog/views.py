from django.shortcuts import render, get_object_or_404
from newsfeed.forms import EmailNewsfeedForm
from blog.models import Post
from django.http import HttpResponse, HttpResponseRedirect, Http404

def reflexion(request, reflexion_id):
	reflexiones = Post.objects.filter(categoria__nombre = 'reflexiones', estado = 'p')
	reflexion = get_object_or_404(reflexiones, pk = reflexion_id)
	context = {
		'reflexion' : reflexion,
	}
	return render(request, 'reflexion.html', context)

def reflexiones(request):

	forma_suscripcion = EmailNewsfeedForm()
	reflexiones       = Post.objects.filter(categoria__nombre = 'reflexiones', estado = 'p')
	audio             = reflexiones.filter(tags__nombre = 'audio')
	video             = reflexiones.filter(tags__nombre = 'video')
	ebook             = reflexiones.filter(tags__nombre = 'ebook')
	context           = {
		'audio'             : audio,
		'video'             : video,
		'ebook'             : ebook,
		'reflexiones' 		: reflexiones,
		'forma_suscripcion' : forma_suscripcion,
	}


	return render(request, 'blog/reflexiones.html', context)


