from django.shortcuts import render,redirect
from .models import Cliente
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import View
@login_required
def index(request):
    context={}
    return render(request, 'tallerdb/index.html', context)
def salir (request):
    logout(request)
    return redirect('/')
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
def inis(request):
    return render(request, "tallerdb/inis.html")
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