from django.urls import path, include
from indumentaria import views

app_name= "indumentaria"

urlpatterns = [
    path("remera/",views.Crear_Remera.as_view(),name="crear_remera"),
    path("remera/crear/",views.Listado_Remera.as_view(),name="listado_remera"),
    path("remera/<int:pk>/",views.Ver_Remera.as_view(),name="ver_remera"),
    path("remera/<int:pk>/editar/",views.Editar_Remera.as_view(),name="editar_remera"),
    path("remera/<int:pk>/eliminar/",views.Eliminar_Remera.as_view(),name="eliminar_remera"),
]
