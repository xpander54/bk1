from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from cgv import views



admin.autodiscover()

urlpatterns = patterns('',
	url(r'^', include('newsfeed.urls')),
	url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^galerias/', include('galerias.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^contacto/$', views.contacto, name = 'contacto'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name' : 'auth/login.html'}),
	url(r'^registro/$', views.registro, name = 'registro'),    
	url(r'^registro/$', views.registro, name = 'registro'),
<<<<<<< HEAD
)
=======
) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

>>>>>>> b57ab9fadf07f61f9e50a1984924165588a891b3
