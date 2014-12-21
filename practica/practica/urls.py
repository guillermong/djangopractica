from django.conf.urls import patterns, include, url
from leercsv import views
from leercsv import api
#from prueba import *
from api import *

maestro_resource = maestroResource()


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

	url(r'^load/$', views.load_info, name='load_info'),
	url(r'^api/', include(maestro_resource.urls)),
	url(r'^$', views.index),	
    # Examples:
    # url(r'^$', 'practica.views.home', name='home'),
    # url(r'^practica/', include('practica.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
