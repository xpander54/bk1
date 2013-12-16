from django.contrib import admin
from archivos.models import Categoria, Archivo


class ArchivosInline(admin.TabularInline):

	model           = Archivo
	extra           = 1
	fields          = ('link', 'archivo', 'creado',)
	readonly_fields = ('link', 'creado',)



class CategoriaAdmin(admin.ModelAdmin):

	inlines = [ArchivosInline]


admin.site.register(Categoria, CategoriaAdmin)