from django.urls import path
from inicio.views import inicio, acerca_de_mi, buscar_zapatilla, crear_zapatilla

urlpatterns = [
     path("", inicio, name="inicio"),
     path("acerca-de-mi/", acerca_de_mi, name="acerca_de_mi"),
     path("buscar-zapatilla/", buscar_zapatilla, name="buscar_zapatilla"),
     path("crear-zapatilla/", crear_zapatilla, name="crear_zapatilla"),
   
]
