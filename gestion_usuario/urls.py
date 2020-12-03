from django.contrib import admin
from django.urls import path
from .views import CrearFuncionario , ListaFuncionario , home , actualizar_Funcionario , EliminarFuncionario , DetalleFuncionario
from django.contrib.auth.views import login_required
urlpatterns = [
    path('crear/', login_required(CrearFuncionario.as_view()), name='crear_usuario'),
    path('listado/', login_required(ListaFuncionario.as_view()), name='lista_usuarios'),
    path('actualizar/<int:pk>', login_required(actualizar_Funcionario), name='actualizar_usuario'),
    path('eliminar/<int:pk>', login_required(EliminarFuncionario.as_view()), name='eliminar_usuario'),
    path('detalle/<int:pk>', login_required(DetalleFuncionario.as_view()), name='detalle_usuario'),


    path('home/', login_required(home) , name='home'),
    



]
