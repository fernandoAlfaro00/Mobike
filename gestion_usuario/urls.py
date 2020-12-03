from django.contrib import admin
from django.urls import path
from .views import CrearFuncionario , ListaFuncionario , home , actualizar_Funcionario

urlpatterns = [
    path('crear/', CrearFuncionario.as_view(), name='crear_usuario'),
    path('listado/', ListaFuncionario.as_view(), name='lista_usuarios'),
    path('actualizar/<int:pk>', actualizar_Funcionario, name='actualizar_usuario'),
    path('home/', home , name='home'),



]
