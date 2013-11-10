from django.shortcuts import render
from newsfeed.forms import EmailNewsfeedForm
from blog.models import Post


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


