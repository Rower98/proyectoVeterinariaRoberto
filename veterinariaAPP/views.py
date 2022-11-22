from django.shortcuts import render, redirect 
from veterinariaAPP.models import Dueno, Mascota, Consulta, Estetica, Vacuna, Cirugia
from veterinariaAPP.forms import *

def index (request):
    return render (request, 'index.html')

def viewdueno(request):
    duenos = Dueno.objects.all()
    return render(request, 'Duenos/viewDuenos.html',{'duenos':duenos})


