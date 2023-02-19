from django.db import models

# Create your models here.
class Club(models.Model):
    nombre = models.CharField(max_length=60)
    agno_fundacion = models.IntegerField()

class DT(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    club = models.CharField(max_length=40)

class Jugador(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    club = models.CharField(max_length=40)
    goles = models.IntegerField()