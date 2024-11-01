from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import formulario_creacion_usuario

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