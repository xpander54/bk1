# -*- encoding: utf-8 -*-

from django.db import models



class Categoria(models.Model):

	nombre      = models.CharField(max_length = 255)
	descripcion = models.TextField(u'descripción', blank = True)
	creado      = models.DateTimeField(u'fecha de creación', auto_now_add = True)
	modificado  = models.DateTimeField(u'última modificación', auto_now = True)


	def __unicode__(self):

		return self.nombre



class Archivo(models.Model):

	categoria = models.ForeignKey(Categoria)
	archivo   = models.FileField(upload_to = 'archivos')
	creado    = models.DateTimeField(u'fecha de creación', auto_now_add = True)

	def link(self):

		if self.archivo:

			return '<a href="/media/%s">Descargar<a>' % self.archivo

		return 'Añadir archivo'

	link.allow_tags        = True
	link.short_description = 'link'

	def __unicode__(self):

		return self.archivo
