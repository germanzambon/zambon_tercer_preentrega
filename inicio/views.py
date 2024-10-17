from django.http import HttpResponse
from django.template import Template, context, loader
from datetime import datetime
from django.shortcuts import render, redirect
from inicio.models import zapatillas
from inicio.forms import CrearZapatillaFormulario, BuscarZapatillaFormulario


def inicio (request):
     return render (request, "index.html")

def acerca_de_mi (request):
    return render (request, "acerca_de_mi.html")

def crear_zapatilla (request):
     
     formulario=CrearZapatillaFormulario()
     
     if request.method == "POST":
          
        formulario=CrearZapatillaFormulario(request.POST)
        if formulario.is_valid():
             data=formulario.cleaned_data 
             zapatilla=zapatillas(marca=data.get("marca"), color=data.get("color"), talle=data.get("talle"))
             zapatilla.save()
             return redirect("buscar_zapatilla")
     
     return render(request,"crear_zapatilla.html",{"form":formulario})
     
     
def buscar_zapatilla (request):
     formulario= BuscarZapatillaFormulario(request.GET)
     if formulario.is_valid():
        marca= formulario.cleaned_data.get("marca")
        color= formulario.cleaned_data.get("color")
        Zapatillas=zapatillas.objects.filter(marca__icontains=marca, color__icontains=color,)
     else:
          Zapatillas=zapatillas.objects.all()
     return render (request, "buscar_zapatilla.html",{"Zapatillas":Zapatillas, "form":formulario})


