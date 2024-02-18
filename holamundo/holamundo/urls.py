"""
URL configuration for holamundo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rescate_perros.views import holamundo, home, perros, ver_perro, lista_perros, ver_perro_api, nuevo_refugio, ver_refugio, editar_refugio, eliminar_refugio, lista_refugios
from Crea.views import ver_propiedades_posible, ver_propiedad, index, captar_propiedad, ver_propiedades_disponibles, ver_propiedaddis, ver_pcliente, ver_pocliente, nueva_propiedad, editar_propiedad, eliminar_propiedad, nuevo_cliente, editar_cliente, eliminar_cliente

urlpatterns = [

    path('accounts/', include('allauth.urls')),


    path('admin/', admin.site.urls),
    path('hola/', holamundo, name='holamundo'),
    path('', home, name='home'),
    path('', home, name='dashboard'),
    path('lista_perros/ciudad/<str:ciudad>/', lista_perros, name='lista_perros'),
    path('perro/<int:codigo_perro>/', ver_perro, name='detalle_perro'),
    path('perro_api/<int:codigo_perro>/', ver_perro_api, name='detalle_perro_api'),
    
    # URLS de APLICACION
    path('refugio/', lista_refugios, name='lista_refugios'),
    path('refugio/<int:codigo_refugio>/', ver_refugio, name='ver_refugio'),
    path('refugio/nuevo/', nuevo_refugio, name='nuevo_refugio'),
    path('refugio/editar/<int:codigo_refugio>/', editar_refugio, name='editar_refugio'),
    path('refugio/eliminar/<int:codigo_refugio>/', eliminar_refugio, name='eliminar_refugio'),

    #
    path('propiedades_posibles/', ver_propiedades_posible, name="ver_propiedades_posible"),
    path('propiedades_disponibles/', ver_propiedades_disponibles),
    path('propiedad/<int:codigo_propiedad>/', ver_propiedad ,name="detalle_propiedad"),
    path('propiedaddis/<int:codigo_propiedad>/', ver_propiedaddis ,name="detalle_propiedaddis"),
    path('captar_propiedad/<int:codigo_propiedad>/', captar_propiedad),
    path('pcliente/', ver_pcliente, name="ver_pcliente"),
    path('cliente/<int:codigo_cliente>/', ver_pocliente, name="detalle_cliente"),
    path('propiedad/nuevo', nueva_propiedad ,name="nueva_propiedad"),
    path('propiedad/editar/<int:codigo_propiedad>/', editar_propiedad ,name="editar_propiedad"),
    path('propiedad/eliminar/<int:codigo_propiedad>/', eliminar_propiedad ,name="eliminar_propiedad"),
    path('cliente/nuevo', nuevo_cliente ,name="nuevo_cliente"),
    path('cliente/editar/<int:codigo_cliente>/', editar_cliente ,name="editar_cliente"),
    path('cliente/eliminar/<int:codigo_cliente>/', eliminar_cliente ,name="eliminar_cliente"),
    

    # Extra_Pages
    path("extra_pages/", include("extra_pages.urls")),
    # layouts
    path("layouts/", include("layouts.urls")),  
 



]
