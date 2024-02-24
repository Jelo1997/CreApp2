from django.contrib import admin
from .models import Cliente, Propiedad_posible, Propiedad_disponible, Empleado

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'apellido',
        'cedula',
        'telefono',
        'correo',
        'observaciones',
        'estado',
    )


@admin.register(Propiedad_posible)
class Propiedad_posibleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'codigo',
        'fecha_registro',
        'ubicacion',
        'precio',
        'tipo',
        'descripcion',
        'es_activo',
        'precio_avaluo',
        'id_cliente',
    )
    list_filter = ('fecha_registro', 'es_activo', 'id_cliente')


@admin.register(Propiedad_disponible)
class Propiedad_disponibleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'codigo',
        'fecha_ingreso',
        'fecha_caducidad',
        'tipo',
        'ubicacion',
        'descripcion',
        'tipo_comision',
        'precio_pactado',
        'precio_comercial',
        'precio_crea',
        'precio_minimo',
        'convenio',
        'proceso',
        'id_cliente',
    )
    list_filter = ('fecha_ingreso', 'fecha_caducidad', 'id_cliente')


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'correo', 'area', 'celular','foto')

