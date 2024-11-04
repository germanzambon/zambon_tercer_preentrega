from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import formulario_creacion_usuario, FormulacioEdicionPerfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtras

def login(request):

    formulario= AuthenticationForm ()
    
    if request.method == "POST":
        formulario= AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            nombre_de_usuario= formulario.cleaned_data.get("username")
            contrasenia= formulario.cleaned_data.get("password")
         
            usuario= authenticate(username= nombre_de_usuario, password= contrasenia)
         
            django_login(request, usuario)
            
            return redirect("inicio")
         
    return render(request,"usuarios/login.html",{"form": formulario} )


def registrarse (request):
    formulario=formulario_creacion_usuario()
    if request.method== "POST":
       formulario=UserCreationForm(request.POST)
       if formulario.is_valid():
            formulario.save()
            return redirect("usuarios:login")
    return render(request,"usuarios/registrarse.html", {"form":formulario})

@login_required
def editar_perfil(request):
    datos_extras, created = DatosExtras.objects.get_or_create(user=request.user)
    formulario=FormulacioEdicionPerfil(instance=request.user, initial={"avatar":datos_extras.avatar})
    
    if request.method == "POST":
        formulario=FormulacioEdicionPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            new_avatar=formulario.cleaned_data["avatar"]
            datos_extras.avatar=new_avatar if new_avatar else datos_extras.avatar
            datos_extras.save()
            
            formulario.save()
            
            return redirect("inicio")
    
    return render(request, "usuarios/editar_perfil.html",{"form":formulario})

class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name= "usuarios/cambiar_password.html"
    success_url= reverse_lazy("usuarios:editar_perfil")