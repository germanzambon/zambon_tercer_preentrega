from django.urls import path
from inicio.views import inicio, zapatilla

urlpatterns = [
     path("", inicio, name="inicio"),
     path("zapatilla/", zapatilla, name="zapatilla"),
]
