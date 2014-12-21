from django.db import models
import datetime

# Create your models here.

class maestro(models.Model):
    articulo = models.CharField(max_length=100,unique= True,null=True,blank=True)
    ean = models.CharField(max_length=20,null=True,blank=True)
    descripcion= models.CharField(max_length=100,null=True,blank=True)
    vigencia = models.CharField(max_length=20,null=True,blank=True)
    marca = models.CharField(max_length=10,null=True,blank=True)
    #stock = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    fechBloqBasico = models.CharField(max_length=100,null=True,blank=True)
    BloqCanalJumbo = models.CharField(max_length=100,null=True,blank=True)
    FechBloqCanalJumbo = models.CharField(max_length=20,null=True,blank=True)
    BloqCanalSisa = models.CharField(max_length=100,null=True,blank=True)
    FechBloqCanalSisa = models.CharField(max_length=20,null=True,blank=True)
    BloqCanalJSuper = models.CharField(max_length=100,null=True,blank=True)
    FechBloqCanalJSuper = models.CharField(max_length=20,null=True,blank=True)
    ful01a = models.CharField(max_length=100,null=True,blank=True)
    ful02b = models.CharField(max_length=100,null=True,blank=True)
    meg03a = models.CharField(max_length=100,null=True,blank=True)
    meg04b = models.CharField(max_length=100,null=True,blank=True)
    pref05_gr = models.CharField(max_length=100,null=True,blank=True)
    pref06_me = models.CharField(max_length=100,null=True,blank=True)
    pref07_pe = models.CharField(max_length=100,null=True,blank=True)
    cmed08_gr = models.CharField(max_length=100,null=True,blank=True)
    cmed09_me = models.CharField(max_length=100,null=True,blank=True)
    cmed10_pe = models.CharField(max_length=100,null=True,blank=True)
    cpal11_me = models.CharField(max_length=100,null=True,blank=True)
    cpal12_pe = models.CharField(max_length=100,null=True,blank=True)
    cpba13_me = models.CharField(max_length=100,null=True,blank=True)
    cpba14_pe = models.CharField(max_length=100,null=True,blank=True)
    mixt15_gr = models.CharField(max_length=100,null=True,blank=True)
    mixt16_me = models.CharField(max_length=100,null=True,blank=True)
    mixt17_pe = models.CharField(max_length=100,null=True,blank=True)
    emer18_gr = models.CharField(max_length=100,null=True,blank=True)
    emer19_me = models.CharField(max_length=100,null=True,blank=True)
    emer20_pe = models.CharField(max_length=100,null=True,blank=True)
    pref21_mini = models.CharField(max_length=100,null=True,blank=True)
    cmed22_mini = models.CharField(max_length=100,null=True,blank=True)
    cpal23_mini = models.CharField(max_length=100,null=True,blank=True)
    cpba24_mini = models.CharField(max_length=100,null=True,blank=True)
    mixt25_mini = models.CharField(max_length=100,null=True,blank=True)
    emer26_mini = models.CharField(max_length=100,null=True,blank=True)
    
    def __unicode__(self):
		return self.articulo
	

