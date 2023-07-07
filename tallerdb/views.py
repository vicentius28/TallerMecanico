from django.shortcuts import render
from .models import Cliente
def index(request):
    context={}
    return render(request, 'tallerdb/index.html', context)