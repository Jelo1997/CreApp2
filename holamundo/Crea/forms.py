from django import forms
from .models import *
class PropiedadForm(forms.ModelForm):
    
    class Meta:
        model = Propiedad_posible
        fields = ['codigo', 'fecha_registro', 'ubicacion', 'precio', 'tipo', 'descripcion', 'precio_avaluo', 'id_cliente']

class CaptarPropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad_disponible 
        fields = ('codigo', 
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
                  'proceso'
                  )
        
class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'cedula', 'telefono', 'correo', 'observaciones']
        
class EmpleadoForm(forms.ModelForm):
    
    class Meta:
        model = Empleado
        fields = ['telefono', 'apellido','area', 'correo', 'nombre']
