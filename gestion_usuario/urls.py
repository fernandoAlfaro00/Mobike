from django.contrib import admin
from django.urls import path
from .views import CrearFuncionario , ListaFuncionario , home , actualizar_Funcionario , EliminarFuncionario , DetalleFuncionario

urlpatterns = [
    path('crear/', CrearFuncionario.as_view(), name='crear_usuario'),
    path('listado/', ListaFuncionario.as_view(), name='lista_usuarios'),
    path('actualizar/<int:pk>', actualizar_Funcionario, name='actualizar_usuario'),
    path('eliminar/<int:pk>', EliminarFuncionario.as_view(), name='eliminar_usuario'),
    path('detalle/<int:pk>', DetalleFuncionario.as_view(), name='detalle_usuario'),


    path('home/', home , name='home'),
    



]
