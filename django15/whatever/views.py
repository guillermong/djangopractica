from django.shortcuts import render
import csv
from whatever.models import *
from django.http import HttpResponseRedirect





def load_info(request):
	reader = csv.reader(open("/home/zev/Desktop/testpractica/Maestra.csv" ,'rU'), delimiter=';')
	for row in reader:
		if row[0] != 'Articulo':
			a = Whatever(articulo=row[0], ean=row[1], descripcion=row[2].decode("latin-1"),vigencia=row[3],marca=row[4],stock=row[5],fechBloqBasico=row[6],BloqCanalJumbo=row[7],FechBloqCanalJumbo=row[8],BloqCanalSisa=row[9],FechBloqCanalSisa=row[10],BloqCanalJSuper=row[11],FechBloqCanalJSuper=row[12],ful01a=row[13],ful02b=row[14],meg03a=row[15],meg04b=row[16],pref05_gr=row[17],pref06_me=row[18],pref07_pe=row[19],cmed08_gr=row[20],cmed09_me=row[21],cmed10_pe=row[22],cpal11_me=row[23],cpal12_pe=row[24],cpba13_me=row[25],cpba14_pe=row[26],mixt15_gr=row[27],mixt16_me=row[28],mixt17_pe=row[29],emer18_gr=row[30],emer19_me=row[31],emer20_pe=row[32],pref21_mini=row[33],cmed22_mini=row[34],cpal23_mini=row[35],cpba24_mini=row[36],mixt25_mini=row[37],emer26_mini=row[38])			
			a.save()
			
			'''maestro1 = maestro();
			maestro1.articulo=row[0]
			maestro1.ean=row[1]
			maestro1.descripcion=row[2].decode("latin-1")
			maestro1.vigencia=row[3]
			maestro1.marca=row[4]
			maestro1.stock=row[5]
			maestro1.echBloqBasico=row[6]
			maestro1.BloqCanalJumbo=row[7]
			maestro1.FechBloqCanalJumbo=row[8]
			maestro1.BloqCanalSisa=row[9]
			maestro1.FechBloqCanalSisa=row[10]
			maestro1.BloqCanalJSuper=row[11]
			maestro1.FechBloqCanalJSuper=row[12]
			maestro1.ful01a=row[13]
			maestro1.ful02b=row[14]
			maestro1.meg03a=row[15]
			maestro1.meg04b=row[16]
			maestro1.pref05_gr=row[17]
			maestro1.pref06_me=row[18]
			maestro1.pref07_pe=row[19]
			maestro1.cmed08_gr=row[20]
			maestro1.cmed09_me=row[21]
			maestro1.cmed10_pe=row[22]
			maestro1.cpal11_me=row[23]
			maestro1.cpal12_pe=row[24]
			maestro1.cpba13_me=row[25]
			maestro1.cpba14_pe=row[26]
			maestro1.mixt15_gr=row[27]
			maestro1.mixt16_me=row[28]
			maestro1.mixt17_pe=row[29]
			maestro1.emer18_gr=row[30]
			maestro1.emer19_me=row[31]
			maestro1.emer20_pe=row[32]
			maestro1.pref21_mini=row[33]
			maestro1.cmed22_mini=row[34]
			maestro1.cpal23_mini=row[35]
			maestro1.cpba24_mini=row[36]
			maestro1.mixt25_mini=row[37]
			maestro1.emer26_mini=row[38]		
			maestro1.save()'''
				
	return HttpResponseRedirect('/')

