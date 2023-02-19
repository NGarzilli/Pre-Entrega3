from django.urls import path

from .views import *

urlpatterns= [
    path('', inicio, name = 'inicio'),
    path('club/', club, name = 'club'),
    path('dt/', dt, name = 'dt'),
    path('jugadores/', jugadores, name = 'jugadores')

]