import datetime
from django.http import HttpResponse
from django.contrib import messages

from django.shortcuts import redirect, render, redirect , get_object_or_404
from django.views.generic import DetailView, FormView
from django.core.validators import ValidationError
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView
from .models import Propiedad_posible, Propiedad_disponible, Cliente, Empleado
from .forms import PropiedadForm , CaptarPropiedadForm, ClienteForm, EmpleadoForm, BuscarPersonaForm, ObservacionesForm
from django.http import HttpResponse

#generar pdf
from django.template.loader import get_template
from weasyprint import HTML



# Create your views here.
   
def generar_convenio_pdf(request, codigo_propiedad):
    # Obtiene los datos específicos del convenio
    
    propiedad = get_object_or_404(Propiedad_disponible, pk=codigo_propiedad)
    cliente = propiedad.id_cliente
    datos_convenio = {
        'nombre_cliente': cliente.nombre + ' ' + cliente.apellido,
        'cedula_cliente': cliente.cedula,
        'tipo_propiedad': propiedad.tipo,
        'ubicacion_propiedad': propiedad.ubicacion,
        'precio_pactado': propiedad.precio_pactado,
        'fecha_ingreso' : propiedad.fecha_ingreso,
        'fecha_caducidad' : propiedad.fecha_caducidad,
    }
    
    # Carga la plantilla HTML del convenio
    template = get_template('convenio.html')

    # Renderiza la plantilla con los datos del convenio
    html_content = template.render(datos_convenio)

    # Convierte el contenido HTML en un documento PDF
    pdf_file = HTML(string=html_content).write_pdf()

    # Devuelve el archivo PDF como respuesta HTTP
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="convenio.pdf"'
    return response

def index(request):
    template = "index.html"
    return render(request, template)

@login_required
def ver_propiedades_posible(request):
    propiedad = Propiedad_posible.objects.all()
    contenido = {
        'propiedad' : propiedad
    }
    
    template = "propiedades_posibles.html"
    return render(request, template, contenido)

@login_required
def nueva_propiedad(request):
    # Verificar si el usuario está autenticado y tiene un empleado asociado
    if not request.user.is_authenticated or not hasattr(request.user, 'empleado'):
        return HttpResponse('Acceso no permitido')

    # Obtener el empleado asociado al usuario
    empleado = request.user.empleado
    
    # Verificar si el empleado es de la categoría "Aprovicionamiento"
    if not empleado.es_aprovicionamiento():
        return HttpResponse('Acceso no permitido')
    
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

@login_required
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

@login_required
def eliminar_propiedad(request, codigo_propiedad):
    contenido = {}
    contenido['propiedad'] = get_object_or_404(Propiedad_posible, pk = codigo_propiedad) 
    contenido['propiedad'].es_activo = False
    contenido['propiedad'].save()
    return redirect('/propiedades_posibles/')

@login_required    
def ver_propiedades_disponibles(request):
    propiedad = Propiedad_disponible.objects.all()
    contenido = {
        'propiedad' : propiedad
    }
    template = "propiedades_disponibles.html"
    return render(request, template, contenido)

@login_required
def ver_propiedad(request, codigo_propiedad):
    propiedad = get_object_or_404(Propiedad_posible, pk = codigo_propiedad )
    cliente = propiedad.id_cliente
    contenido = {
        'propiedad' : propiedad,
        'cliente': cliente,
    }
    template = "propiedad.html"
    return render(request, template, contenido)

@login_required
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


@login_required
def captar_propiedad(request, codigo_propiedad):
    propiedad = Propiedad_posible.objects.get(pk=codigo_propiedad)

    if request.method == 'POST':
        form = CaptarPropiedadForm(request.POST, instance=propiedad)

        if form.is_valid():
            # Migrar datos y crear nueva instancia en `propiedad_disponible`
            nueva_propiedad = Propiedad_disponible(
                foto_propiedad=form.cleaned_data['foto_propiedad'],
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
                id_cliente=form.cleaned_data['id_cliente_id'] # Add missing fields if needed (id_cliente, etc.)
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

@login_required
def ver_pcliente(request):
    cliente = Cliente.objects.all()
    contenido = {
        'cliente' : cliente
    }
    template = "pcliente.html"
    return render(request, template, contenido)

@login_required
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

@login_required
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

@login_required
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

@login_required
def ver_empleado(request):
    empleado = Empleado.objects.all()
    contenido = {
        'empleado' : empleado
    }
    template = "empleado.html"
    return render(request, template, contenido)

@login_required
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

@login_required
def editar_empleado(request, codigo_empleado):
    contenido = {}
    empleado = get_object_or_404(Empleado, pk = codigo_empleado) 
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES, instance=empleado)               
        if form.is_valid():
            form.save()
            return redirect(empleado.get_absolute_url())
    else:
        form = EmpleadoForm(instance=empleado)
    contenido['form'] = form
    contenido['empleado'] = empleado
    return render(request, 'formulario_empleado.html', contenido)

@login_required
def eliminar_empleado(request, codigo_empleado):
    contenido = {}
    contenido['empleado'] = get_object_or_404(Empleado, pk = codigo_empleado) 
    contenido['empleado'].delete()
    return redirect('/empleado/')

@login_required
def ver_perfil_empleado(request):
    
    if not request.user.is_authenticated or not hasattr(request.user, 'empleado'):
        return render(request, 'error.html', {'mensaje': 'No tienes permiso para acceder a esta página'})
    
    empleado = request.user.empleado
    
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES, instance=empleado)
        if form.is_valid():
            form.save()
            messages.success(request, 'Información actualizada exitosamente.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Error al actualizar la información. Por favor, revisa los campos.')
    else:
        form = EmpleadoForm(instance=empleado)

    contenido = {
        'empleado': empleado,
        'form': form,
    }
    return render(request, 'det_empleado.html', contenido)

@login_required
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
    
class BuscarPersonaView(FormView):
    template_name = "realizarconsulta.html"
    form_class = BuscarPersonaForm

    def form_valid(self, form):
        cedula = form.cleaned_data['cedula']
        return propiedades_por_usuario(self.request, cedula)  # Llama a la vista de función propiedades_por_usuario

def propiedades_por_usuario(request, cedula):
    cliente = Cliente.objects.get(cedula=cedula)
    propiedades_disponibles = Propiedad_disponible.objects.filter(id_cliente_id=cliente)
    propiedades_posibles = Propiedad_posible.objects.filter(id_cliente_id=cliente)
    context = {
        "cliente": cliente,
        "propd": propiedades_disponibles,
        "propp": propiedades_posibles,
    }
    return render(request, "consulta.html", context) 

def procesos_propiedades(request):
    cliente = Cliente.objects.all
    propiedades_disponibles = Propiedad_disponible.objects.all
    context={
        "cliente": cliente,
        "propd": propiedades_disponibles,
    }
    return render(request, "procesos.html", context) 


def actualizar_proceso(request, propiedad_id):
 if request.method == 'POST':
        propiedad = Propiedad_disponible.objects.get(pk=propiedad_id)
        nuevo_proceso_valor = request.POST.get('proceso')
        nuevo_proceso_etiqueta = None
        
        # Buscar la etiqueta del nuevo proceso
        for valor, etiqueta in propiedad.proc2:
            if valor == nuevo_proceso_valor:
                nuevo_proceso_etiqueta = etiqueta
                break
        
        nuevas_observaciones = request.POST.get('observaciones')
        
        # Actualizar los datos de la propiedad
        propiedad.proceso_venta = nuevo_proceso_etiqueta
        propiedad.observaciones_procesos = nuevas_observaciones
        propiedad.save()
        return redirect('procesos propiedades')

class ClienteDetailView(DetailView):
    model = Cliente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ObservacionesForm()
        return context

def agregar_observaciones(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        form = ObservacionesForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data) 
            observacion = form.cleaned_data['observaciones_adicionales']
            cliente.observaciones_adicionales += observacion + '\n'
            cliente.save()
            
    else:
        form = ObservacionesForm()
        print(form.errors)

    context = {'cliente': cliente, 'form': form}
    return render(request, "ppcliente.html", context)


