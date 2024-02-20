import datetime
from msilib.schema import ListView
from django.shortcuts import redirect, render, get_object_or_404

from django.core.validators import ValidationError
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Propiedad_posible, Propiedad_disponible, Cliente, Empleado, Perfil_Usuario
from .forms import PropiedadForm , CaptarPropiedadForm, ClienteForm, EmpleadoForm, Perfil_UsuarioForm


# Create your views here.
@login_required
def ver_perfil_usuario(request):
    contenido = {}
    if hasattr(request.user, 'perfil'):
        perfil = request.user.perfil
    else:
        perfil = Perfil_Usuario(user = request.user)
    if request.method == 'POST':
        form = Perfil_UsuarioForm(request.POST, request.FILES, instance=perfil)               
        if form.is_valid():
            form.save()
    else:
        form = Perfil_UsuarioForm(instance=perfil)
    contenido['form'] = form
    contenido['empleado'] = perfil
    
    return render(request, 'perfil_usuario.html',contenido)
    
    
    
def index(request):
    template = "index.html"
    return render(request, template)

def ver_propiedades_posible(request):
    propiedad = Propiedad_posible.objects.all()
    contenido = {
        'propiedad' : propiedad
    }
    
    template = "propiedades_posibles.html"
    return render(request, template, contenido)

def nueva_propiedad(request):
    contenido = {}
    if request.method == 'POST':
        contenido['form'] = PropiedadForm(
                        request.POST or None,
                        request.FILES or None,)
        if contenido['form'].is_valid():
            contenido['form'].save()
            return redirect(contenido['form'].instance.get_absolute_url())
        
    contenido['instancia_propiedad'] = Propiedad_posible()
    contenido ['form'] = PropiedadForm(
        request.POST or None,
        request.FILES or None,
        instance = contenido['instancia_propiedad']
    )
    
    return render(request, 'formulario_propiedad.html', contenido)

def editar_propiedad(request, codigo_propiedad):
    contenido = {}
    propiedad = get_object_or_404(Propiedad_posible, pk = codigo_propiedad) 
    if request.method == 'POST':
        form = PropiedadForm(request.POST, request.FILES, instance=propiedad)               
        if form.is_valid():
            form.save()
            return redirect(propiedad.get_absolute_url())
    else:
        form = PropiedadForm(instance=propiedad)
    contenido['form'] = form
    contenido['propiedad'] = propiedad
    return render(request, 'formulario_propiedad.html', contenido)

def eliminar_propiedad(request, codigo_propiedad):
    contenido = {}
    contenido['propiedad'] = get_object_or_404(Propiedad_posible, pk = codigo_propiedad) 
    contenido['propiedad'].es_activo = False
    contenido['propiedad'].save()
    return redirect('/propiedades_posibles/')
    
def ver_propiedades_disponibles(request):
    propiedad = Propiedad_disponible.objects.all()
    contenido = {
        'propiedad' : propiedad
    }
    template = "propiedades_disponibles.html"
    return render(request, template, contenido)

def ver_propiedad(request, codigo_propiedad):
    propiedad = get_object_or_404(Propiedad_posible, pk = codigo_propiedad )
    cliente = propiedad.id_cliente
    contenido = {
        'propiedad' : propiedad,
        'cliente': cliente,
    }
    template = "propiedad.html"
    return render(request, template, contenido)

def ver_propiedaddis(request, codigo_propiedad):
    c = {}
    propiedaddis =  get_object_or_404(Propiedad_disponible, pk=codigo_propiedad)
    cliente = propiedaddis.id_cliente
    contenido ={
        'propiedad': propiedaddis,
        'cliente': cliente,
    }
    template = "propiedaddis.html"
    return render(request,template, contenido)



def captar_propiedad(request, codigo_propiedad):
    propiedad = Propiedad_posible.objects.get(pk=codigo_propiedad)

    if request.method == 'POST':
        form = CaptarPropiedadForm(request.POST, instance=propiedad)

        if form.is_valid():
            # Migrar datos y crear nueva instancia en `propiedad_disponible`
            nueva_propiedad = Propiedad_disponible(
                codigo=form.cleaned_data['codigo'],
                fecha_ingreso=datetime.date.today(),  # Set fecha_ingreso to today
                fecha_caducidad=form.cleaned_data.get('fecha_caducidad'),  # Optional field
                tipo=form.cleaned_data['tipo'],
                ubicacion=form.cleaned_data['ubicacion'],
                descripcion=form.cleaned_data['descripcion'],
                tipo_comision=form.cleaned_data['tipo_comision'],
                precio_pactado=form.cleaned_data.get('precio_pactado'),  # Optional field
                precio_comercial=form.cleaned_data['precio_comercial'],
                precio_crea=form.cleaned_data['precio_crea'],
                precio_minimo=form.cleaned_data['precio_minimo'],
                convenio=form.cleaned_data['convenio'],
                proceso='Proceso de Venta',  # Default processo to "Proceso de Venta"
                # Add missing fields if needed (id_cliente, etc.)
            )
            nueva_propiedad.save()
            propiedad.es_activo = False
            propiedad.save()
            return redirect('/propiedades_disponibles')
 
    else:
        form = CaptarPropiedadForm(instance=propiedad)

    context = {
        'form': form,
    }

    return render(request, 'captar_propiedad.html', context)

def ver_pcliente(request):
    cliente = Cliente.objects.all()
    contenido = {
        'cliente' : cliente
    }
    template = "pcliente.html"
    return render(request, template, contenido)

def nuevo_cliente(request):
    contenido = {}
    if request.method == 'POST':
        contenido['form'] = ClienteForm(
                        request.POST or None,
                        request.FILES or None,)
        if contenido['form'].is_valid():
            contenido['form'].save()
            return redirect(contenido['form'].instance.get_absolute_url())
        
    contenido['instancia_cliente'] = Cliente()
    contenido ['form'] = ClienteForm(
        request.POST or None,
        request.FILES or None,
        instance = contenido['instancia_cliente']
    )
    
    return render(request, 'formulario_cliente.html', contenido)

def editar_cliente(request, codigo_cliente):
    contenido = {}
    cliente = get_object_or_404(Cliente, pk = codigo_cliente) 
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)               
        if form.is_valid():
            form.save()
            return redirect(cliente.get_absolute_url())
    else:
        form = ClienteForm(instance=cliente)
    contenido['form'] = form
    contenido['cliente'] = cliente
    return render(request, 'formulario_cliente.html', contenido)

def eliminar_cliente(request, codigo_cliente):
    contenido = {}
    contenido['cliente'] = get_object_or_404(Cliente, pk = codigo_cliente) 
    contenido['cliente'].delete()
    return redirect('/pcliente/')

def ver_pocliente(request, codigo_cliente):


    cliente = get_object_or_404(Cliente, pk = codigo_cliente )


    contenido = {
        "cliente" :cliente,
     
    }
    template = "ppcliente.html"
    return render(request, template, contenido)

def ver_empleado(request):
    empleado = Empleado.objects.all()
    contenido = {
        'empleado' : empleado
    }
    template = "empleado.html"
    return render(request, template, contenido)

def nuevo_empleado(request):
    contenido = {}
    if request.method == 'POST':
        contenido['form'] = EmpleadoForm(
                        request.POST or None,
                        request.FILES or None,)
        if contenido['form'].is_valid():
            contenido['form'].save()
            return redirect(contenido['form'].instance.get_absolute_url())
        
    contenido['instancia_empleado'] = Empleado()
    contenido ['form'] = EmpleadoForm(
        request.POST or None,
        request.FILES or None,
        instance = contenido['instancia_empleado']
    )
    
    return render(request, 'formulario_empleado.html', contenido)

def editar_empleado(request, codigo_empleado):
    contenido = {}
    empleado = get_object_or_404(Cliente, pk = codigo_empleado) 
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=empleado)               
        if form.is_valid():
            form.save()
            return redirect(empleado.get_absolute_url())
    else:
        form = ClienteForm(instance=empleado)
    contenido['form'] = form
    contenido['cliente'] = empleado
    return render(request, 'formulario_cliente.html', contenido)

def eliminar_empleado(request, codigo_empleado):
    contenido = {}
    contenido['empleado'] = get_object_or_404(Empleado, pk = codigo_empleado) 
    contenido['empleado'].delete()
    return redirect('/empleado/')

def ver_det_empleado(request, codigo_empleado):


    empleado = get_object_or_404(Empleado, pk = codigo_empleado )


    contenido = {
        "empleado" :empleado,
     
    }
    template = "det_empleado.html"
    return render(request, template, contenido)

def index(request):
    template = 'dashboard.html'
    c = {
        'titulo': 'ESTA ES TU CASA',
        'mensaje': 'Este es un mensaje desde la vista home'
    }
    return render(request, template, c)
    