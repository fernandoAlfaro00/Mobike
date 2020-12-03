from django.db import models
from django.contrib.auth.models import User


    
    

    


class Funcionario(models.Model):

        
    GENERO_CHOICES = [
        ('M' , 'Masculino'),
        ('F' , 'Femenino'),
        ('O' , 'Otro')


    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genero =  models.CharField(max_length=20 , choices=GENERO_CHOICES)
    area   =models.CharField(max_length=30)
    

    
    

    class Meta:
        verbose_name = 'funcionario'
        verbose_name_plural = 'funcionarios'


    def __str__(self):

        return self.user.username
        
        
    

