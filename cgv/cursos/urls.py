from django.conf.urls import patterns, include, url
from cursos import views


urlpatterns = patterns('',
	url(r'cursos/$', views.cursos, name = 'cursos'),
	#url(r'reflexion/$', views.reflexion, name = 'reflexion'),
	#url(r'^(?P<reflexion_id>\d+)/reflexion/$', views.reflexion, name = 'reflexion'),
)
