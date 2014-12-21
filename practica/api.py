from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import DjangoAuthorization
from tastypie.constants import ALL
from leercsv.models import *
from django.db.models import *



class maestroResource(ModelResource):
    class Meta:
		queryset = maestro.objects.all().filter(vigencia="Vigente")
		#queryset = maestro.objects.values('marca','vigencia').annotate(porcentaje=Sum('stock'))
		#print (queryset)
		resource_name = 'maestro'
		fields = ['marca','vigencia','stock']
		limit = 0
		#excludes = ['FechBloqCanalJSuper']
        #filtering = { "Vigente" : "vigencia" }
        
