from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ingresarDatos', views.ingresar_datos , name='ingresar_datos'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),

]
