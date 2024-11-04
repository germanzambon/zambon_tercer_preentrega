from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class formulario_creacion_usuario(UserCreationForm):
    username=forms.CharField(label="usuario")
    email= forms.EmailField()
    password1=forms.CharField(label="contrasenia", widget=forms.PasswordInput)
    password2=forms.CharField(label="repetir contrasenia", widget=forms.PasswordInput)
    first_name=forms.CharField(label="nombre")
    last_name=forms.CharField(label="apellido")
    
    class meta:
        model= User
        fields = ["Username","email","first_name","last_name","password1","password2"]
        help_texts = {key: "" for key in fields}
        
class FormulacioEdicionPerfil(UserChangeForm):
    email= forms.EmailField()
    first_name=forms.CharField(label="nombre")
    last_name=forms.CharField(label="apellido")
    password= None
    avatar= forms.ImageField(required=False)
    
    class Meta:
        model= User
        fields= ["email","first_name","last_name", "avatar"]