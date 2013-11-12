from django.conf.urls import patterns, include, url
from django.contrib import admin
import views



admin.autodiscover()

urlpatterns = patterns('',
	url(r'^', include('newsfeed.urls')),
	url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^Contacto/$', views.contacto, name = 'contacto'),
    
)
