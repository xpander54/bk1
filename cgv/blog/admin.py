# -*- encoding: utf-8 -*-

from django.contrib import admin
from blog.models import Categoria, Tag, Post, Comentario


class PostAdmin(admin.ModelAdmin):

	fieldsets = [
		(
			None,
			{
				'fields' : ['titulo', 'abstract', 'contenido', 'estado', 'destacado']
			}
		),
		(
			'Categorización',
			{
				'fields' : ['categoria', 'tags']
			}
		),
		(
			'Extra',
			{
				'fields' : ['usuario', 'creado', 'modificado']
			}
		),
	]
	filter_horizontal = ('tags',)
	readonly_fields = ('usuario', 'creado', 'modificado',)


	def save_model(self, request, obj, form, change):

		if not change:
			obj.usuario = request.user

		obj.save()


	class Media:

		js = [
			'admin/js/tinymce/tinymce.min.js',
			'admin/js/tinymce/config.js'
		]



admin.site.register(Categoria)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comentario)