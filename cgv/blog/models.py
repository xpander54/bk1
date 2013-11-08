# -*- encoding: utf-8 -*-

from django.db import models
from django.conf import settings


class Categoria(models.Model):

	nombre      = models.CharField(max_length = 100)
	descripcion = models.TextField(u'descripción', blank = True)
	creado      = models.DateTimeField(u'fecha de creación', auto_now_add = True)
	modificado  = models.DateTimeField(u'última modificación', auto_now = True)

	def __unicode__(self):

		return self.nombre


	class Meta:

		verbose_name = u'categoría'



class Tag(models.Model):

	nombre      = models.CharField(max_length = 100)
	descripcion = models.TextField(blank = True)
	creado      = models.DateTimeField(u'fecha de creación', auto_now_add = True)
	modificado  = models.DateTimeField(u'última modificación', auto_now = True)

	def __unicode__(self):

		return self.nombre



class Post(models.Model):

	ESTADO = (
		('b', 'Borrador'),
		('a', 'Aprobación Pendiente'),
		('p', 'Publicado'),
	)

	usuario    = models.ForeignKey(settings.AUTH_USER_MODEL)
	categoria  = models.ForeignKey(Categoria, verbose_name = u'categoría')
	tags       = models.ManyToManyField(Tag)
	titulo     = models.CharField(u'título', max_length = 255)
	abstract   = models.TextField(u'resumen', blank = True)
	contenido  = models.TextField(blank = True)
	estado     = models.CharField(max_length = 1, default = 'b', choices = ESTADO)
	destacado  = models.BooleanField(default = False)
	creado     = models.DateTimeField(u'fecha de creación', auto_now_add = True)
	modificado = models.DateTimeField(u'última modificación', auto_now = True)

	def __unicode__(self):

		return self.titulo


class Comentario(models.Model):

	email      = models.EmailField(max_length = 100)
	comentario = models.TextField()
	aprobado   = models.BooleanField(default = False)
	creado     = models.DateTimeField(u'fecha de creación', auto_now_add = True)
	modificado = models.DateTimeField(u'última modificación', auto_now = True)

	def __unicode__(self):

		return self.email
