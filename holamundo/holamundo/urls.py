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
from holamundo import views
from django.contrib.auth.decorators import login_required
from .views import MyPasswordChangeView, MyPasswordSetView
from django.conf import settings
from django.conf.urls.static import static

from Crea.views import BuscarPersonaView, ver_propiedades_posible, ver_propiedad, index, captar_propiedad, ver_propiedades_disponibles, ver_propiedaddis, ver_pcliente, ver_pocliente, nueva_propiedad, editar_propiedad, eliminar_propiedad, nuevo_cliente, editar_cliente, eliminar_cliente, ver_empleado, nuevo_empleado, editar_empleado, eliminar_empleado, ver_det_empleado, propiedades_por_usuario,ver_perfil_empleado, generar_convenio_pdf, agregar_observaciones, procesos_propiedades, actualizar_proceso


urlpatterns = [

    


    path('admin/', admin.site.urls),
    
    path('', views.DashboardView.as_view(), name='dashboard'),
    # calender
    path('calendar', views.CalendarView.as_view(), name='calendar'),
    # Email
    path("email/", include("e_mail.urls")),
    # Components
    path("components/", include("components.urls")),
    # Extra_Pages
    path("extra_pages/", include("extra_pages.urls")),
    # Extra_Pages
    path("email_templates/", include("email_templates.urls")),
    # layouts
    path("layouts/", include("layouts.urls")),  
    # Authentication
    path("authentication/", include("authentication.urls")),  
    
    path(
        "account/password/change/",
        login_required(MyPasswordChangeView.as_view()),name="account_change_password",),
    path(
        "account/password/set/",
        login_required(MyPasswordSetView.as_view()),name="account_set_password",),  
 
    path('accounts/', include('allauth.urls')),

    #
    path('propiedades_posibles/', ver_propiedades_posible, name="ver_propiedades_posible"),
    path('propiedades_disponibles/', ver_propiedades_disponibles, name ="ver_propiedades_disponible"),
    path('propiedad/<int:codigo_propiedad>/', ver_propiedad , name="detalle_propiedad"),
    path('propiedaddis/<int:codigo_propiedad>/', ver_propiedaddis , name="detalle_propiedaddis"),
    path('captar_propiedad/<int:codigo_propiedad>/', captar_propiedad),
    path('propiedad/nuevo', nueva_propiedad ,name="nueva_propiedad"),
    path('propiedad/editar/<int:codigo_propiedad>/', editar_propiedad ,name="editar_propiedad"),
    path('propiedad/eliminar/<int:codigo_propiedad>/', eliminar_propiedad ,name="eliminar_propiedad"),
    
    path('pcliente/', ver_pcliente, name="ver_pcliente"),
    path('cliente/<int:codigo_cliente>/', ver_pocliente, name="detalle_cliente"),
    path('cliente/nuevo', nuevo_cliente ,name="nuevo_cliente"),
    path('cliente/editar/<int:codigo_cliente>/', editar_cliente ,name="editar_cliente"),
    path('cliente/eliminar/<int:codigo_cliente>/', eliminar_cliente ,name="eliminar_cliente"),
    
    path('empleado/', ver_empleado, name="ver_empleado"),
    path('accounts/profile/', ver_perfil_empleado, name="ver_perfil_empleado"),
    path('empleado/<int:codigo_empleado>/', ver_det_empleado, name="detalle_empleado"),
    path('empleado/nuevo', nuevo_empleado ,name="nuevo_empleado"),
    path('empleado/editar/<int:codigo_empleado>/', editar_empleado ,name="editar_empleado"),
    path('empleado/eliminar/<int:codigo_empleado>/', eliminar_empleado ,name="eliminar_empleado"),

    path("consulta/<str:cedula>/", propiedades_por_usuario, name='consulta'),

    path("consultapersona", BuscarPersonaView.as_view(), name='consultapersona'),
    
    #convenio
    path('convenio/<int:codigo_propiedad>/', generar_convenio_pdf, name='convenio'),

    path('procesos', procesos_propiedades, name="procesos propiedades"),
    path('actualizar_proceso/<int:propiedad_id>/', actualizar_proceso, name='ruta_para_actualizar_proceso'),
    path('cliente/<int:id>/agregar_observaciones/', agregar_observaciones, name='agregar_observaciones'),

]
urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)