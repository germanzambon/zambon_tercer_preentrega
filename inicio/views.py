from django.http import HttpResponse
from django.template import Template, context, loader
from datetime import datetime
from django.shortcuts import render
from inicio.models import zapatillas

def inicio (request):
     return render (request, "index.html")

def zapatilla (request):
    return render (request, "zapatilla.html")


