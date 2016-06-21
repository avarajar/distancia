from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'distance.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'calculate.views.home', name='home'),
    url(r'^calcular/', 'calculate.views.calcular', name='calcular'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': settings.MEDIA_ROOT, } ),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': settings.STATIC_ROOT, } ),
   )