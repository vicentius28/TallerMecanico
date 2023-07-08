from django.shortcuts import render,redirect
from .models import Cliente
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
def nav(request):
    return render(request, 'tallerdb/nav.html',)
def crud(request):
    clientes=Cliente.objects.all()
    return render(request, 'tallerdb/crud.html', {'clientes':clientes})
def index(request):
    context={}
    return render(request, 'tallerdb/index.html', context)
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
    return redirect('/')
def edit(request,rut):
    cliente=Cliente.objects.get(rut=rut)
    return render(request,"tallerdb/edit.html",{"cliente":cliente})
def editar(request):
    rut=request.POST["txtRut"]
    nombre=request.POST["txtNombre"]
    aPaterno=request.POST["txtApellidoP"]
    aMaterno=request.POST["txtApellidoM"]
    telefono=request.POST["txtTelefono"]
    email=request.POST["txtEmail"]
    direccion=request.POST["txtDireccion"]
    activo=request.POST["txtActivo"]
    cliente=Cliente.objects.get(rut=rut)
    cliente.rut=rut
    cliente.nombre=nombre
    cliente.apellido_paterno=aPaterno
    cliente.apellido_materno=aMaterno
    cliente.telefono=telefono
    cliente.email=email
    cliente.direccion=direccion
    cliente.activo=activo
    cliente.save()
    return redirect('/')
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
    return redirect('/')
def regis(request):
    return render(request, "tallerdb/regis.html")
def cli_del(request,pk):
    context={}
    try:
        cliente=Cliente.objects.get(rut=pk)
        cliente.delete
        mensa="Bien, datos eliminados"
        clientes=Cliente.objects.all()
        context={'clientes':clientes,'mensa':mensa}
        return render(request,'tallerdb/crud.html',context)
    except:
        mensa="Error, rut no existe"
        clientes=Cliente.objects.all()
        context={'clientes':clientes,'mensa':mensa}    
    return render(request, "tallerdb/crud.html",context)
def cli_edit(request,pk):
    if pk!="":
        cliente=Cliente.objects.all(rut=pk)
        context={'cliente':Cliente}
        if cliente:
            return render(request,'tallerdb/crud.html',context)
        else:
            context={'mensa':"Error, rut no existe"}
        return render(request, "tallerdb/crud.html")    
def upd(request):
    if request.method=="POST":
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"
        cliente=Cliente()
        cliente.rut=rut
        cliente.nombre=nombre
        cliente.apellido_paterno=aPaterno
        cliente.apellido_materno=aMaterno
        cliente.telefono=telefono
        cliente.email=email
        cliente.direccion=direccion
        cliente.activo=1
        cliente.save()

        return render(request, "tallerdb/crud.html")  
def menu(request):
    request.session["usuario"]="cgarcia"
    usuario=request.session["usuario"]
    context={'usuario':usuario}
    return render(request, "administrador/menu.html",context)    

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