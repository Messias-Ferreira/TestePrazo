from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Constituicao(models.Model):
    titulo = models.CharField(max_length=255)
    capitulo = ArrayField(models.CharField(max_length=255,blank=True,null=True))
    secao = ArrayField(models.CharField(max_length=255,blank=True,null=True))
    subsecao =  ArrayField(models.CharField(max_length=255,blank=True,null=True))
    trecho = models.TextField()
    pagina_inicial = models.IntegerField()
    


