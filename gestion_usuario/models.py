from django.db import models
from django.contrib.auth.models import User


    
    

    


class Funcionario(models.Model):

        
        
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genero =  models.CharField(max_length=20)
    area   =models.CharField(max_length=30)
    

    
    

    class Meta:
        verbose_name = 'funcionario'
        verbose_name_plural = 'funcionarios'


    def __str__(self):

        return self.user.username
        
        
    

