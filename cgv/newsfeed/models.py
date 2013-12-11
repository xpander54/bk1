# -*- encoding: utf-8 -*-


from django.db import models


class Feed(models.Model):

    nombre      = models.CharField(max_length = 200)
    descripcion = models.TextField(u'descripción', blank = True)
    creado      = models.DateTimeField(u'fecha de creación', auto_now_add = True)
    modificado  = models.DateTimeField(u'última modificación', auto_now = True)

    def __unicode__(self):
    	return self.nombre


class Suscriptor(models.Model):

	feed       = models.ForeignKey(Feed)
	email      = models.EmailField(max_length = 100, unique = True)
	activo     = models.BooleanField(default = False)
	creado     = models.DateTimeField(u'fecha de creación', auto_now_add = True)
	modificado = models.DateTimeField(u'última modificación', auto_now = True)
	codigo     = models.CharField(u'código', max_length = 10)

	def __unicode__(self):
		return self.email
