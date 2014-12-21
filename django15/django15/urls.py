from django.conf.urls import patterns, include, url
from whatever.api import WhateverResource
from whatever.models import *
from django.db.models import *
from whatever import views

whatever_resource = WhateverResource()

urlpatterns = patterns('',
   url(r'^api/', include(whatever_resource.urls)),
   url(r'^load/$', views.load_info, name='load_info'),

)
