from django.shortcuts import render
from .models import Cliente
def nav(request):
    return render(request, 'tallerdb/nav.html',)
def index(request):
    context={}
    return render(request, 'tallerdb/index.html', context)
def index(request):
    context={}
    return render(request, 'tallerdb/index.php', context)
def frenos(request):
    return render(request, "tallerdb/frenos.html")
def equipo(request):
    return render(request, "tallerdb/equipo.html")
def otros(request):
    return render(request, "tallerdb/otros.html")
def inis(request):
    return render(request, "tallerdb/inis.html")
def regis(request):
    return render(request, "tallerdb/regis.html")