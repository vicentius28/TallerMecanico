from django.shortcuts import render,redirect,get_object_or_404
from .models import Cliente, Producto, Boleta, detalle_boleta
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from tallerdb.compra import Carrito

def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    producto =get_object_or_404 (Producto,id_producto=id)
    cantidad_restar = 1
    producto.stock -= cantidad_restar
    carrito_compra.agregar(producto=producto)
    producto.save()
    return redirect('tienda')
    
def eliminar_producto(request,id):
    carrito_compra= Carrito(request)
    producto = get_object_or_404 (Producto,id_producto=id)
    cantidad_restar = 1
    producto.stock += cantidad_restar
    carrito_compra.eliminar(producto=producto)
    
    return redirect('tienda')
def restar_producto(request,id):
    carrito_compra= Carrito(request)
    producto = get_object_or_404 (Producto,id_producto=id)
    cantidad_restar = 1
    producto.stock += cantidad_restar
    carrito_compra.restar(producto=producto)
    producto.save()
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra = Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')

def generarBoleta(request):
    precio_total=0
    for key,value in request.session['carrito'].items():
        precio_total = precio_total+ int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productoss=[]
    for key,value in request.session['carrito'].items():
            producto = Producto.objects.get(id_producto = value['id_producto'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_pro = producto, cantidad= cant, subtotal = subtotal)
            detalle.save()
            productoss.append(detalle)
    datos={
        'productos':productoss,
        'fecha':boleta.fechaCompra,
        'total':boleta.total
    }
    request.session['boleta']= boleta.id_boleta
    carrito= Carrito(request)
    carrito.limpiar()
    return render(request, 'tallerdb/detallecarrito.html',datos)



def tienda(request):
    return render(request, 'tallerdb/tienda.html')


def tienda(request):
    productos=Producto.objects.all()
    return render(request, 'tallerdb/tienda.html', {'productos':productos})

def index(request):
    return render(request, 'tallerdb/index.html')
def profile(request):
    return render(request, 'account/profile.html')
def crud(request):
    clientes=Cliente.objects.all()
    return render(request, 'tallerdb/crud.html', {'clientes':clientes})
    
def frenos(request):
    return render(request, "tallerdb/frenos.html")
def marcas(request):
    return render(request, "tallerdb/marcas.html")
def equipo(request):
    return render(request, "tallerdb/equipo.html")
def otros(request):
    return render(request, "tallerdb/otros.html")


def eliminar(request,rut):
    cliente=Cliente.objects.get(rut=rut)
    cliente.delete()
    return redirect('crud')
def edit(request,rut):
    cliente=Cliente.objects.get(rut=rut)
    return render(request,"tallerdb/edit.html",{"cliente":cliente})
def editar(request):
    rut=request.POST['txtRut']
    nombre=request.POST['txtNombre']
    apellido_paterno=request.POST['txtApellidoP']
    apellido_materno=request.POST['txtApellidoM']
    telefono=request.POST['txtTelefono']
    email=request.POST['txtEmail']
    direccion=request.POST['txtDireccion']
    activo=request.POST['txtActivo']
    cliente=Cliente.objects.get(rut=rut)
    cliente.rut=rut
    cliente.nombre=nombre
    cliente.apellido_paterno=apellido_paterno
    cliente.apellido_materno=apellido_materno
    cliente.telefono=telefono
    cliente.email=email
    cliente.direccion=direccion
    cliente.activo=activo
    cliente.save()
    return redirect('crud')
def registrar(request):
    rut=request.POST['txtRut']
    nombre=request.POST['txtNombre']
    apellido_paterno=request.POST['txtApellidoP']
    apellido_materno=request.POST['txtApellidoM']
    telefono=request.POST['txtTelefono']
    email=request.POST['txtEmail']
    direccion=request.POST['txtDireccion']
    activo=request.POST['txtActivo']
    cliente=Cliente.objects.create(rut=rut,nombre=nombre,apellido_paterno=apellido_paterno,
    apellido_materno=apellido_materno,telefono=telefono,email=email,direccion=direccion,activo=activo)
    return redirect('crud')
def regis(request):
    return render(request, "tallerdb/regis.html")

def get (self,request,*args,**kwargs):
    if request.user.is_authenticated:
        return render(self.template_name)
    else:
        return redirect('login')

def contactar(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        fono = request.POST['fono']
        subject = 'CONTACTO'+' '+name
        mensaje = request.POST['mensaje']

        template = render_to_string('tallerdb/email_template.html',{
            'name': 'nombre: '+ name,
            'email': 'email: '+ email,
            'fono': 'telefono: '+fono,
            'message':'mensaje: '+mensaje
        })

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['vic.fariasm@duocuc.cl']


        )

        email.fail_silently = False
        email.send()
        
        messages.success(request,'Se ha enviado tu correo.')
        return redirect('index')