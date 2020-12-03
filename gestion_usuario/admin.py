from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib import admin
from django import forms
from .models import Funcionario 
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User




# class CustomUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model = User


# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User

        
        
# class CustomUserAdmin(UserAdmin):
#     form = CustomUserChangeForm
#     add_form = CustomUserCreationForm
#     fieldsets = UserAdmin.fieldsets


# @admin.register(Funcionario)
# class PatientAdmin(admin.ModelAdmin):

#     add_fieldsets = (
#     (None, {
#         'classes': ('wide',),
#         'fields': ('email', 'username', 'password1', 'password2',)
#     }),
# )
#     list_display = (
#         'genero',
#         'area'
#     )



# admin.site.register(User , UsuarioFuncionarioAdmin)



admin.site.register(Funcionario)