from django.shortcuts import render
from django.http import HttpResponse


from AppCoder.models import Club

# Create your views here.
def club(request):
    club = Club(nombre= 'Chelsea Football Club', agno_fundacion='1905')
    club.save()
    respuesta= f'Club: {club.nombre}, Año fundacion: {club.agno_fundacion}'

    return HttpResponse(respuesta)