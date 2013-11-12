from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
import views



admin.autodiscover()

urlpatterns = patterns('',
	url(r'^', include('newsfeed.urls')),
	url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^Contacto/$', views.contacto, name = 'contacto'),
) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)