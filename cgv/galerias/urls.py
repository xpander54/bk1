from django.conf.urls import patterns, include, url
from galerias import views

urlpatterns = patterns('',
	url(r'galerias/$', views.galerias, name = 'galerias'),
)