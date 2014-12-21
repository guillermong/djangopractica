"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from leercsv.views import *
from leercsv.models import *
from django.core.urlresolvers import reverse
import csv


class SimpleTest(TestCase):
	
	def test_process(self):
		f = open("/home/zev/Desktop/testpractica/Maestra.csv", "rbU")
		reader = csv.reader(f, delimiter=';')
		for row in reader:
			if row[0] != 'Articulo':
				if maestro.objects.filter(articulo=row[0]):
					continue
				else:
					return maestro.objects.create(articulo=row[0], ean=row[1], descripcion=row[2].decode("latin-1"),vigencia=row[3],marca=row[4],stock=int(row[5]),fechBloqBasico=row[6],BloqCanalJumbo=row[7],FechBloqCanalJumbo=row[8],BloqCanalSisa=row[9],FechBloqCanalSisa=row[10],BloqCanalJSuper=row[11],FechBloqCanalJSuper=row[12],ful01a=row[13],ful02b=row[14],meg03a=row[15],meg04b=row[16],pref05_gr=row[17],pref06_me=row[18],pref07_pe=row[19],cmed08_gr=row[20],cmed09_me=row[21],cmed10_pe=row[22],cpal11_me=row[23],cpal12_pe=row[24],cpba13_me=row[25],cpba14_pe=row[26],mixt15_gr=row[27],mixt16_me=row[28],mixt17_pe=row[29],emer18_gr=row[30],emer19_me=row[31],emer20_pe=row[32],pref21_mini=row[33],cmed22_mini=row[34],cpal23_mini=row[35],cpba24_mini=row[36],mixt25_mini=row[37],emer26_mini=row[38])


	def test_maestro(self):
		a = test_process()
		self.assertTrue(isinstance(a, maestro))
        self.assertEqual(a.__unicode__,a.articulo)
        
    def test_api(self):
		
		url = reverse(views.load_info)
		self.client.get(url)
		self.assertEqual(resp.status_code, 200)
