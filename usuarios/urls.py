from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView

app_name= "usuarios"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("registrarse/", views.registrarse, name="registrarse"),
    path("perfil/editar/", views.editar_perfil, name="editar_perfil"),
    path("perfil/editar/password", views.CambiarPassword.as_view(), name="cambiar_password"),
    path("logout/", LogoutView.as_view(template_name="usuarios/logout.html"), name="logout"),

]
