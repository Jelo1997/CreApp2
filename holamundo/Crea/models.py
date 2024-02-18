from django import forms
from django.db import models
from django.urls import reverse

# Create your models here.


#MODELO CLIENTE

class Cliente(models.Model):
    nombre = models.CharField(max_length=144, blank= False, null= False)
    apellido = models.CharField(max_length=144, blank= False, null= False)
    cedula = models.CharField(max_length=144, blank= False, null= False)
    telefono = models.CharField(max_length=144, blank= False, null= False)
    correo = models.EmailField(max_length=144, blank= False, null= False)
    observaciones = models.CharField(max_length=144, blank= False, null= False)

    def __str__(self) -> str:
       return f'{self.nombre}'

    def get_absolute_url(self):


       return reverse("detalle_cliente", kwargs={'codigo_cliente' : self.id})
   
    def get_edit_url(self):
       return reverse("editar_cliente", kwargs={'codigo_cliente' : self.id})
   
    def get_delete_url(self):


       return reverse("eliminar_cliente", kwargs={'codigo_cliente' : self.id})


    
#MODELO PROPIEDAD DISPONIBLE

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
    



  
#MODELO PROPIEDAD DISPONIBLE


       return reverse("eliminar_cliente", kwargs={'codigo_cliente' : self.id})

class Propiedad_disponible(models.Model):
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
        ("Proceso de Venta", "Proceso de Venta"),
        ("Vendida", "Vendida"),
        ("Jurídico", "Jurídico")
    )
    proceso = models.CharField(max_length=20, choices=proc)
    id_cliente = models.ForeignKey(Cliente, related_name ='pk', on_delete=models.CASCADE, null= True)

    def __str__(self) -> str:
       return f'{self.codigo}'
    
#MODELO EMPLEADO    

class Empleado(models.Model):
    nombre = models.CharField(max_length=144, blank= False, null= True)
    apellido = models.CharField(max_length=144, blank= False, null= True)
    correo  = models.EmailField(max_length=144, blank= False, null= True)
    areas = (
        ("Aprobicionamiento", "Aprobicionamiento"),
        ("Ventas", "Ventas"),
        ("Tramites", "Tramites"),
    )
    area = models.CharField(max_length=50, choices=areas, blank= False, null= True)
    telefono = models.CharField(max_length=144, blank= False, null= True)
    
    def __str__(self) -> str:
       return f'{self.nombre}'
    
    
