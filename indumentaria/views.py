from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from indumentaria.models import remera
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class Crear_Remera(LoginRequiredMixin, CreateView):
    model = remera
    template_name = "indumentaria/crear_remera.html"
    success_url= reverse_lazy("indumentaria:listado_remera")
    fields= ("color", "talle")

class Listado_Remera(ListView):
    model= remera
    template_name= "indumentaria/listado_remera.html"
    context_object_name= "remera"
    
class Ver_Remera(DetailView):
    model = remera
    template_name = "indumentaria/ver_remera.html"
    
class Editar_Remera(LoginRequiredMixin, UpdateView):
    model = remera
    template_name = "indumentaria/editar_remera.html"
    success_url= reverse_lazy("indumentaria:listado_remera")
    fields= ("color", "talle")
    
class Eliminar_Remera(LoginRequiredMixin, DeleteView):
    model = remera
    template_name = "indumentaria/eliminar_remera.html"
    success_url= reverse_lazy("indumentaria:listado_remera")

