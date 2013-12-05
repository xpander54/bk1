from django.http import HttpResponse
from django.shortcuts import render 
from django.conf.urls import patterns
from django.contrib import admin
from django.core.mail import send_mass_mail, BadHeaderError
from newsfeed.models import Feed, Suscriptor


class SuscriptorAdmin(admin.ModelAdmin):

	list_display = ('__unicode__', 'activo', 'codigo', 'creado')

	def get_urls(self):

		urls    = super(SuscriptorAdmin, self).get_urls()
		my_urls = patterns('',
			(r'my_view/$', self.admin_site.admin_view(self.my_view)),
		)

		return my_urls + urls

	def my_view(self, request):

		if request.method == 'POST': #{

			lista_users = []
			titulo      = request.POST.get('titulo')
			feed        = request.POST.get('feed')
			feed_users  = Suscriptor.objects.filter(feed__nombre__iexact = 'feed principal', activo = True)

			for feed_user in feed_users: #{

				lista_users.append((titulo, feed, 'netorcido@gmail.com', [feed_user.email]))

			#}

			try: #{

				send_mass_mail(lista_users, fail_silently=False)
			
			#}

			except BadHeaderError: #{

				return HttpResponse("Errores de Cabeceras!")

			#}

			return HttpResponse("Hecho!")

		#}


		return render(request, 'newsfeed/admin/my_view.html')


class FeedAdmin(admin.ModelAdmin):

	fieldsets = [
		(
			None,
			{
				'fields' : ['nombre', 'descripcion',]
			}
		),
		(
			'Extra',
			{
				'fields' : ['creado', 'modificado',]
			}
		)
	]
	list_display = ('__unicode__', 'creado', 'modificado',)
	readonly_fields = ('creado', 'modificado',)
	


admin.site.register(Feed, FeedAdmin)
admin.site.register(Suscriptor, SuscriptorAdmin)