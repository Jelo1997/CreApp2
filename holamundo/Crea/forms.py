from django import forms 
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit


class PropiedadForm(forms.ModelForm):
    
    
    class Meta:
        model = Propiedad_posible
        fields = ['codigo', 'fecha_registro', 'ubicacion', 'precio', 'tipo', 'descripcion', 'precio_avaluo','foto_propiedad', 'id_cliente']

class CaptarPropiedadForm(forms.ModelForm):
  class Meta:
    model = Propiedad_disponible
    fields = [
      'foto_propiedad',
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
    ]
    widgets = {
    'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
    'fecha_caducidad': forms.DateInput(attrs={'type': 'date'}),
  }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
      Fieldset(
        'Datos de la propiedad',
        'codigo',
        'fecha_ingreso',
        'fecha_caducidad',
        'tipo',
        'ubicacion',
        'descripcion',
      ),
      Fieldset(
        'Datos económicos',
        'tipo_comision',
        'precio_pactado',
        'precio_comercial',
        'precio_crea',
        'precio_minimo',
      ),
      Fieldset(
        'Información adicional',
        'convenio',
        'proceso',
        'id_cliente_id'
      ),
      Submit('submit', 'Captar'),
    )

        
class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'cedula', 'telefono', 'correo', 'observaciones', 'estado']

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = ['celular', 'apellido', 'correo', 'nombre', 'foto']

class BuscarPersonaForm(forms.Form):
  cedula = forms.CharField(label="Cédula", max_length=10)

class ObservacionesForm(forms.Form):
      observaciones_adicionales = forms.CharField(widget=forms.Textarea, label="Observaciones adicionales")