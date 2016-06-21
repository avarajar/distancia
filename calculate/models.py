from django.db import models

# Create your models here.


class Ciudad(models.Model):
    nombre = models.CharField(max_length=60, null=True, blank=True, verbose_name='Nombre')
    latitud = models.CharField(max_length=140, null=True, blank=True, verbose_name='Latitud')
    longitud = models.CharField(max_length=140, null=True, blank=True, verbose_name='Longitud')

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Ciudade"


class Distance(models.Model):
    origen = models.CharField(max_length=60, null=True, blank=True, verbose_name='Origen')
    destino = models.CharField(max_length=60, null=True, blank=True, verbose_name='Destino')
    distancia = models.CharField(max_length=140, null=True, blank=True, verbose_name='Distancia')

    def __unicode__(self):
        return self.origen

    class Meta:
        verbose_name = "Distancia"
