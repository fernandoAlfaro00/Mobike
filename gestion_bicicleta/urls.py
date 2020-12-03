from django.contrib import admin
from django.urls import path
from .views import CrearBicicleta , ModificarBicicleta , DetalleBicicleta , ListaBicicleta , EliminarBicicleta

urlpatterns = [
    path('crear/', CrearBicicleta.as_view(), name='crear_bicicleta'),
    path('listado/', ListaBicicleta.as_view(), name='listado_bicicleta'),
    path('<pk>/actualizar', ModificarBicicleta.as_view(), name='actualizar_bicicleta'),
    path('<int:pk>/detalle', DetalleBicicleta.as_view(), name='detalle_bicicleta'),
    path('<int:pk>/eliminar', EliminarBicicleta.as_view(), name='eliminar_bicicleta'),


    



]
