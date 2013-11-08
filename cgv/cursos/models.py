# -*- encoding: utf-8 -*-

from django.db import models
from django.conf import settings


class Curso(models.Model):

	titulo     = models.CharField(u'título',max_length = 255)
	abstract   = models.TextField(blank = True)
	contenido  = models.TextField(blank = True)
	creado     = models.DateTimeField(u'fecha de creación', auto_now_add = True)
	modificado = models.DateTimeField(u'última modificación', auto_now = True)

	def __unicode__(self):

		return self.titulo


class Ciclo(models.Model):

	usuario    = models.ForeignKey(settings.AUTH_USER_MODEL)
	curso      = models.ForeignKey(Curso)
	inicio     = models.DateTimeField(u'Fecha de contratación', auto_now_add = True)
	expiracion = models.DateTimeField(u'Fecha de Expiración')
