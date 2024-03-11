from django import forms
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


#MODELO CLIENTE
   
class Cliente(models.Model):
    nombre = models.CharField(max_length=144, blank= False, null= False)
    apellido = models.CharField(max_length=144, blank= False, null= False)
    cedula = models.CharField(max_length=144, blank= False, null= False)
    telefono = models.CharField(max_length=144, blank= False, null= False)
    correo = models.EmailField(max_length=144, blank= False, null= False)
    observaciones = models.CharField(max_length=144, blank= False, null= False)
    estados = (
        ("Comprador", "Comprador"),
        ("Vendedor", "Vendedor"),
        ("Comprador/Vendedor", "Comprador/Vendedor"),
    )
    estado = models.CharField(max_length=45, choices=estados, null=True)
    caracteristicas = (
        ("Vendido", "Vendido"),
        ("En Seguimiento", "En Seguimiento"),
        ("Descartado", "Descartado"),
    )
    caracteristica = models.CharField(max_length=45, choices=caracteristicas, null=True)  
    def __str__(self) -> str:
       return f'{self.nombre}'

    def get_absolute_url(self):
       return reverse("detalle_cliente", kwargs={'codigo_cliente' : self.id})
   
    def get_edit_url(self):
       return reverse("editar_cliente", kwargs={'codigo_cliente' : self.id})
   
    def get_delete_url(self):
       return reverse("eliminar_cliente", kwargs={'codigo_cliente' : self.id})


    
#MODELO PROPIEDAD POSIBLE

class Propiedad_posible(models.Model):
    codigo = models.CharField(max_length=144, blank= False, null= False)
    fecha_registro = models.DateField()
    ubicacion = models.CharField(max_length=144, blank= False, null= False)
    precio = models.DecimalField(max_digits=65, decimal_places = 2 ,blank = False, null = False)
    tipos = (
        ("Casa", "Casa"),
        ("Terreno", "Terreno"),
    )
    tipo = models.CharField(max_length=15, choices=tipos)  
    descripcion = models.TextField(max_length=500, blank= False, null= False)
   # image = models.ImageField(upload_to="propiedades")
    es_activo = models.BooleanField(blank=False, null=False, default=True, 
                                    verbose_name='¿Propiedad activa?')
    precio_avaluo = models.DecimalField(max_digits=65, decimal_places = 2 ,blank = False, null = False)
    foto_propiedad = models.FileField(
      upload_to="foto_propiedad/",
      blank=True,
    )
    id_cliente = models.ForeignKey( Cliente, related_name ='id_cliente', on_delete=models.CASCADE, null= True)


    def __str__(self) -> str:

       return f'{self.tipo, self.precio, self.codigo, self.es_activo}'
   
    def get_absolute_url(self):
       return reverse("detalle_propiedad", kwargs={'codigo_propiedad' : self.pk})
   
    def get_edit_url(self):
       return reverse("editar_propiedad", kwargs={'codigo_propiedad' : self.pk})

       return f'{self.es_activo , self.tipo, self.precio, self.codigo}'

    
    def get_delete_url(self):
       return reverse("eliminar_propiedad", kwargs={'codigo_propiedad' : self.pk})
    


#MODELO EMPLEADO    

class Empleado(models.Model):
    user = models.OneToOneField(User, related_name='empleado', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=144, blank= False, null= True)
    apellido = models.CharField(max_length=144, blank= False, null= True)
    correo  = models.EmailField(max_length=144, blank= False, null= True)
    areas = (
        ("Aprovicionamiento", "Aprovicionamiento"),
        ("Ventas", "Ventas"),
        ("Tramites", "Tramites"),
        ("Gerencia", "Gerencia"),
    )
    area = models.CharField(max_length=50, choices=areas, blank= False, null= True)
    celular = models.CharField(max_length=144, blank= False, null= True)
    foto = models.FileField(
      upload_to="foto_empleado/",
      blank=True,
    )
    def __str__(self) -> str:
       return f'{self.nombre}'
    
    def get_absolute_url(self):
      return reverse("detalle_empleado", kwargs={'codigo_empleado' : self.id})
   
    def get_edit_url(self):
      return reverse("editar_empleado", kwargs={'codigo_empleado' : self.id})
   
    def get_delete_url(self):
      return reverse("eliminar_empleado", kwargs={'codigo_empleado' : self.id})

    def es_aprovicionamiento(self):
      return self.area == "Aprovicionamiento"

    def es_ventas(self):
      return self.area == "Ventas"

    def es_tramites(self):
        return self.area == "Tramites"
    
    def es_gerencia(self):
        return self.area == "Gerencia"
  
#MODELO PROPIEDAD DISPONIBLE


       

class Propiedad_disponible(models.Model):
    foto_propiedad = models.FileField(
      upload_to="foto_propiedad/",
      blank=True,
    )
    codigo = models.CharField(max_length=144, blank= False, null= False)
    fecha_ingreso = models.DateField()
    fecha_caducidad = models.DateField()
    tipos = (
        ("Casa", "Casa"),
        ("Terreno", "Terreno"),
    )
    tipo = models.CharField(max_length=15, choices=tipos)
    ubicacion = models.CharField(max_length=144, blank= False, null= False)
    descripcion = models.TextField(max_length=500, blank= False, null= False)
    comision =(
        ("Fijo", "Fijo"),
        ("Porcentaje", "Porcentaje")
    )
    tipo_comision = models.CharField(max_length=15, choices=comision)
    precio_pactado = models.DecimalField(max_digits=65, decimal_places = 2 ,blank = True, null = True)
    precio_comercial = models.DecimalField(max_digits=65, decimal_places = 2 ,blank = False, null = False)
    precio_crea = models.DecimalField(max_digits=65, decimal_places = 2 ,blank = False, null = False)
    precio_minimo = models.DecimalField(max_digits=65, decimal_places = 2 ,blank = False, null = False)
    conv = (
        ("En Convenio", "En Convenio"),
        ("Sin Convenio", "Sin Convenio")
    )
    convenio = models.CharField(max_length=20, choices=conv)
    proc = (
        ("Contado", "Contado"),
        ("Credito", "Credito"),
    )
    proceso = models.CharField(max_length=20, choices=proc)
    proc2 = (
        ("1", "Levantamiento planimétrico de compra y venta (1 semana)"),
        ("2", "Aprobación de la planimetría en el municipio (3 semanas)"),
        ("3", "Minuta y documentación en notaria (4 días)"),
        ("4", "Ingreso de la carpeta en notaria (3 días)"),
        ("5", "Espera para la asignación de un perito evaluador (3 semanas)"),
        ("6", "Aprobación de perito evaluador (3 días)"),
        ("7", "Crédito aprobado"),
        ("8", "Firmas de traspaso de dominio en notaria"),
        ("9", "Registro del crédito hipotecario en el municipio(3 días)"),
        ("10", "Fin"),
    )
    proc3 = (
        ("1", "Levantamiento planimétrico de compra y venta (1 semana)"),
        ("2", "Aprobación de la planimetría en el municipio (3 semanas)"),
        ("3", "Minuta y documentación en notaria (4 días)"),
        ("4", "Ingreso al departamento de rentas en el municipio (1 semana)"),
        ("5", "Pago de alcabalas y plusvalía"),
        ("6", "Reingreso a la notaría para la revisión (3 días)"),
        ("7", "Firmas de la compra y venta en notaria (2 dias)"),
        ("8", "Registro de las escrituras en el municipio (3 dias )"),
        ("9", "Fin Compra y venta de contado"),
    )
    proceso_venta = models.CharField(max_length=60, choices=proc2, null=True)
    observaciones_procesos = models.TextField(max_length=500, blank= False, null= True)
    id_cliente = models.ForeignKey(Cliente, related_name ='pk', on_delete=models.CASCADE, null= True)
    def __str__(self) -> str:
       return f'{self.codigo}'

class Proceso(models.Model):
   id_cliente = models.ForeignKey(Cliente, related_name ='id_procesocliente', on_delete=models.CASCADE, null= True)
   id_empleado = models.ForeignKey(Empleado, related_name ='id_procesoempleado', on_delete=models.CASCADE, null= True)
   id_propiedad = models.ForeignKey(Propiedad_disponible, related_name ='id_procesopropiedad1', on_delete=models.CASCADE, null= True)
   def __str__(self) -> str:
    return f'{self.id_cliente}'

class Observaciones(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='observaciones')
    observacion = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Observación de {self.cliente.nombre} - {self.fecha_creacion}'

    class Meta:
        ordering = ['-fecha_creacion']
     