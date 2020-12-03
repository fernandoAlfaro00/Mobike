from django.contrib import admin
from django.urls import path
from .views import CrearCliente , actualizar_cliente , EliminarCliente , ListaCliente ,DetalleCliente

urlpatterns = [
    path('crear/', CrearCliente.as_view(), name='crear_cliente'),
    path('listado/', ListaCliente.as_view(), name='lista_clientes'),
    path('actualizar/<int:pk>', actualizar_cliente, name='actualizar_cliente'),
    path('eliminar/<int:pk>', EliminarCliente.as_view(), name='actualizar_cliente'),
    path('detalle/<int:pk>', DetalleCliente.as_view(), name='actualizar_cliente'),





]
