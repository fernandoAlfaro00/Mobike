from django.contrib import admin
from django.urls import path
from .views import CrearFuncionario , ListaFuncionario , ActulizarFuncionario

urlpatterns = [
    path('funcionario/crear', CrearFuncionario.as_view(), name='crear_funcionario'),
    path('funcionario/listado', ListaFuncionario.as_view(), name='lista_funcionario'),
    path('funcionario/actualizar/<int:pk>', ActulizarFuncionario, name='actualizar_funcionario'),



]
