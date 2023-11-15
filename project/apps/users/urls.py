from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("perfil/detail/<int:pk>", views.PerfilDetail.as_view(), name="perfil_detail"),
    path("perfil/create/", views.PerfilCreate.as_view(), name="perfil_create"),
    path("perfil/update/<int:pk>", views.PerfilUpdate.as_view(), name="perfil_update"),
    path("perfil/delete/<int:pk>", views.PerfilDelete.as_view(), name="perfil_delete"),
]
