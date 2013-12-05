from django.conf.urls import patterns, include, url
from blog import views


urlpatterns = patterns('',
	url(r'reflexiones/$', views.reflexiones, name = 'reflexiones'),
	url(r'reflexion/$', views.reflexion, name = 'reflexion'),
)
