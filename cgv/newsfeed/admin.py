from django.http import HttpResponse
from django.shortcuts import render 
from django.conf.urls import patterns
from django.contrib import admin
from newsfeed.models import Feed, Subscriptor


class SubscriptorAdmin(admin.ModelAdmin):

	list_display = ('__unicode__', 'activo', 'codigo', 'creado')

	def get_urls(self):

		urls    = super(SubscriptorAdmin, self).get_urls()
		my_urls = patterns('',
			(r'^my_view/$', self.admin_site.admin_view(self.my_view)),
		)

		return my_urls + urls

	def my_view(self, request):

		if request.method == 'POST':

			return HttpResponse('ES POST!')

		return render(request, 'newsfeed/admin/my_view.html')
	


admin.site.register(Feed)
admin.site.register(Subscriptor, SubscriptorAdmin)