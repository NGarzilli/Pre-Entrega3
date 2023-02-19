from django.shortcuts import render
from django.http import HttpResponse


#from AppCoder.models import Club

# Create your views here.


def inicio(request):
    return render(request, 'AppCoder/inicio.html')


def club(request):
    return render(request, 'AppCoder/club.html')


def dt(request):
    return render(request, 'AppCoder/dt.html')


def jugadores(request):
    return render(request, 'AppCoder/jugadores.html')