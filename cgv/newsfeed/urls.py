from django.conf.urls import patterns, include, url
from newsfeed import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
	url(r'^(?P<code>[a-z A-Z 0-9]{10})/newsfeed-confirm/$', views.newsfeed_confirm, name = 'newsfeedconfirm'),
	url(r'^(?P<code>[a-z A-Z 0-9]{10})/newsfeed-deactivate/$', views.newsfeed_deactivate, name = 'newsfeeddeactivate'),
)