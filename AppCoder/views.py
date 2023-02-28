from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Club, Dt, Jugador
from .forms import ClubFormulario, DtFormulario, JugadoresFormulario

# Create your views here.


def inicio(request):
    return render(request, 'AppCoder/inicio.html')


def club(request):
    return render(request, 'AppCoder/club.html')


def dt(request):
    return render(request, 'AppCoder/dt.html')


def jugadores(request):
    return render(request, 'AppCoder/jugadores.html')

def club_formulario(request):

    if request.method == 'POST':
        formulario = ClubFormulario(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data
            club = Club(nombre=datos['nombre'], agno_fundacion=datos['agno_fundacion'])
            club.save()
            return render(request, 'AppCoder/inicio.html')

    formulario = ClubFormulario()   
    return render(request, 'AppCoder/club-formulario.html', {'club_formulario': formulario})

def Dt_formulario(request):
 
    if request.method == 'POST':
        formulario = DtFormulario(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data
            dt = Dt(nombre=datos['nombre'], apellido=datos['apellido'], club=datos['club'])
            dt.save()
            return render(request, 'AppCoder/inicio.html')

    formulario = DtFormulario()   
    return render(request, 'AppCoder/dt-formulario.html', {'dt_formulario': formulario})

def jugadores_formulario(request):
 
    if request.method == 'POST':
        formulario = JugadoresFormulario(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data
            jugador = Jugador(nombre=datos['nombre'], apellido=datos['apellido'], club=datos['club'], goles=datos['goles'])
            jugador.save()
            return render(request, 'AppCoder/inicio.html')

    formulario = JugadoresFormulario()   
    return render(request, 'AppCoder/jugadores-formulario.html', {'jugadores_formulario': formulario})

def buscar_club(request):
    return render(request, 'AppCoder/buscar-club.html')

def buscar(request):
    if request.GET['club']:
        mi_club = request.GET['club']
        resultado= Club.objects.filter(nombre__icontains = mi_club)

        return render(request, 'AppCoder/resultado-busqueda.html', {'nombre': resultado, 'club': mi_club})

    respuesta = 'No se encuentra el club en la base de datos'
    return HttpResponse(respuesta)