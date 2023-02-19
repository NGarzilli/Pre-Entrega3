from django.db import models

# Create your models here.
class Club(models.Model):
    nombre = models.CharField(max_length=60)
    agno_fundacion = models.IntegerField()
    #sigla= models.CharField(max_length=6)

    def __str__(self):
        return self.nombre #+ '(' + str(self.sigla) +')'

class DT(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    club = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre +  ' ' + self.apellido + ' (' + self.club + ')'

class Jugador(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    club = models.CharField(max_length=40)
    goles = models.IntegerField()

    def __str__(self):
        return self.nombre +  ' ' + self.apellido + ' (' + self.club + ')'