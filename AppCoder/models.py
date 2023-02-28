from django.db import models

# Create your models here.
class Club(models.Model):
    nombre = models.CharField(max_length=60)
    agno_fundacion = models.IntegerField()
    
    class Meta:
        verbose_name_plural = 'Clubes'

    def __str__(self):
        return self.nombre 

class Dt(models.Model):
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

    class Meta:
        verbose_name_plural = 'Jugadores'

    def __str__(self):
        return self.nombre +  ' ' + self.apellido + ' (' + self.club + ')'