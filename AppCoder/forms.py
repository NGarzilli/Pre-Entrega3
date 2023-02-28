from django import forms

class ClubFormulario(forms.Form):
        nombre = forms.CharField()
        agno_fundacion = forms.IntegerField()

class DtFormulario(forms.Form):
        nombre = forms.CharField()
        apellido = forms.CharField()
        club = forms.CharField()

class JugadoresFormulario(forms.Form):
        nombre = forms.CharField()
        apellido = forms.CharField()
        club = forms.CharField()
        goles = forms.IntegerField()