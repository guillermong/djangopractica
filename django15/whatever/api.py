from tastypie.resources import ModelResource
from tastypie.constants import ALL
from whatever.models import Whatever
from django.db.models import *
from itertools import *
from django.db import connection


class WhateverResource(ModelResource):
    class Meta:
        queryset = Whatever.objects.all().filter(vigencia='Vigente').annotate(porcentaje=Sum('stock'))
        #queryset = Whatever.objects.values('marca','vigencia').annotate(porcentaje=Sum('stock'))
        fields = ['articulo','marca','stock','porcentaje']
        #print queryset
        #resource_name = 'whatever'
        filtering = { "title" : ALL }        
        limit = 0
