from django.urls import path
from inicio.views import inicio, zapatilla, buscar_zapatilla, crear_zapatilla

urlpatterns = [
     path("", inicio, name="inicio"),
     path("zapatilla/", zapatilla, name="zapatilla"),
     path("buscar-zapatilla/", buscar_zapatilla, name="buscar_zapatilla"),
     path("crear-zapatilla/", crear_zapatilla, name="crear_zapatilla"),
]
