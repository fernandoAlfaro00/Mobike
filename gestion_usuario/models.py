from django.db import models
from django.contrib.auth.models import User


    
    

    


class Funcionario(models.Model):

        
        
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_personal = models.EmailField()
    genero =  models.CharField(max_length=20)
    area   =models.CharField(max_length=30)
    

    
    

    class Meta:
        verbose_name = 'funcionario'
        verbose_name_plural = 'funcionarios'


    def __str__(self):

        return self.user.username
        
        
    



class  Cliente(models.Model):


    COMUNA_CHOICES  = [
        ('RE' , 'Comuna la reina'),
        ('PRO' , 'Comuna providencia'),
        ('FL' , 'Comuna la florida')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=18)
    fecha_nac =  models.DateField()
    tarjeta = models.CharField(max_length=35)
    domicilio = models.CharField(max_length=31)
    comuna = models.CharField(max_length=31, choices= COMUNA_CHOICES , default='RE')
    genero = models.CharField(max_length=10)
    tipo_relacion =  models.CharField(max_length=10)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    
    def __str__(self):

        return self.user.username
        
        
    