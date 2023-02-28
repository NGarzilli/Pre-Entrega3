from django.urls import path

from .views import *

urlpatterns= [
    path('', inicio, name = 'inicio'),
    path('club/', club, name = 'club'),
    path('dt/', dt, name = 'dt'),
    path('jugadores/', jugadores, name = 'jugadores'),
    path('club-formulario/',  club_formulario, name='club-formulario'),
    path('dt-formulario/',  Dt_formulario, name='dt-formulario'),
    path('jugadores-formulario/',  jugadores_formulario, name='jugadores-formulario'),
    path('buscar-club/', buscar_club, name='buscar-club'),
    path('buscar/', buscar, name='buscar')

]