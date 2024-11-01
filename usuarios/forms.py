from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class formulario_creacion_usuario(UserCreationForm):
    email= forms.EmailField()
    password1=forms.CharField(label="contrasenia", widget=forms.PasswordInput)
    password2=forms.CharField(label="repetir contrasenia", widget=forms.PasswordInput)
    
    class meta:
        model= User
        fields = ["Username","email","password1","password2"]
        help_texts = {key: "" for key in fields}