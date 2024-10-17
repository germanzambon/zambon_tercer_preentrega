from django import forms

class CrearZapatillaFormulario(forms.Form):
    marca=forms.CharField(max_length=20)
    color=forms.CharField(max_length=20)
    talle=forms.IntegerField()

class BuscarZapatillaFormulario(forms.Form):
    marca=forms.CharField(max_length=20, required=False)
    color=forms.CharField(max_length=20, required=False)
    