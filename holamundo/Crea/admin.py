from django.contrib import admin
from .models import Propiedad_disponible, Propiedad_posible, Cliente, Empleado
# Register your models here.

@admin.register(Propiedad_posible)
class PropiedadPAdmin(admin.ModelAdmin):
    list_display = ('id','es_activo', 'tipo', 'precio')

@admin.register(Propiedad_disponible)
class PropiedadDAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', )