from django.db import models
from django.contrib.auth.models import User


class Persona(models.Model):

    nombre  = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email =  models.EmailField()
    estado = models.BooleanField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:

        abstract = True 

    

    


class Funcionario(Persona):
    
    email_corporativo = models.EmailField()
    genero =  models.CharField(max_length=20)
    area   =models.CharField(max_length=30)
    



class  Cliente(Persona):

    COMUNA_CHOICES  = [
        ('RE' , 'Comuna la reina'),
        ('PRO' , 'Comuna providencia'),
        ('FL' , 'Comuna la florida')
    ]
    rut = models.CharField(max_length=18)
    fecha_nac =  models.DateField()
    tarjeta = models.CharField(max_length=35)
    domicilio = models.CharField(max_length=31)
    comuna = models.CharField(max_length=31, choices= COMUNA_CHOICES , default='RE')
    genero = models.CharField(max_length=10)
    tipo_relacion =  models.CharField(max_length=10)


    