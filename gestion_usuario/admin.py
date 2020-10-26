from django.contrib.auth.forms import UserCreationForm
from django.contrib import admin
from .models import Cliente ,Funcionario 
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class UserCreationFormExtended(UserCreationForm): 
    def __init__(self, *args, **kwargs): 
        super(UserCreationFormExtended, self).__init__(*args, **kwargs) 


class UsuarioAdmin(UserAdmin):
   

    add_form = UserCreationFormExtended
        

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'first_name','last_name','email' , 'username', 'password1', 'password2',)
        }),
    )
        

class funcionarioAdmin(UserAdmin):


    list_display =  ( 'email_personal','genero','area' )

    


    

admin.site.register(Funcionario)

admin.site.register(Cliente)