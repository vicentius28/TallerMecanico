from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required



urlpatterns= [
    #templates
    path('',views.index, name='index'),
    path('index',views.index,name='index'),
    path('frenos',login_required(views.frenos),name='frenos'),
    path('equipo',login_required(views.equipo),name='equipo'),
    path('marcas',login_required(views.marcas),name='marcas'),
    path('otros',login_required(views.otros),name='otros'),
    #crud
    path('crud',login_required(views.crud),name='crud'),
    path('registrar/',views.registrar),
    path('elim/<rut>', views.eliminar ),
    path('edit/<rut>', views.edit),
    path('editar/',views.editar),
    path('accounts/profile/', views.profile, name='profile'),
    #carrito
    path('tienda/',login_required(views.tienda), name="tienda"),
    path('generarBoleta/',views.generarBoleta, name="generarBoleta"),
    path('agregar/<id>',views.agregar_producto, name="agregar"),
    path('restar/<id>',views.restar_producto, name="restar"),
    path('eliminar/<id>',views.eliminar_producto, name="eliminar"),
    path('limpiar/',views.limpiar_carrito, name="limpiar"),
    


]