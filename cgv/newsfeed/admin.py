from django.contrib import admin
from newsfeed.models import Feed, Subscriptor


class SubscriptorAdmin(admin.ModelAdmin):

	list_display = ('__unicode__', 'activo', 'codigo', 'creado')
	


admin.site.register(Feed)
admin.site.register(Subscriptor, SubscriptorAdmin)