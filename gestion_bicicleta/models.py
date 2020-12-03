from django.db import models


class Bicicleta(models.Model):

    
    codigo = models.CharField(max_length=15 , unique=True , blank=False) 
    estacion = models.CharField(max_length=20 )
    estado  =  models.BooleanField(default=True)
    fecha_modificacion = models.DateTimeField(auto_now=False , auto_now_add=True)
    fecha_inicio  = models.DateTimeField(auto_now=True  , auto_now_add=False)

    def __str__(self):

        return self.codigo

    class Meta:
        verbose_name = 'bicicleta'
        verbose_name_plural = 'bicicletas'

    