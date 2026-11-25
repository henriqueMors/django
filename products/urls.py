from django.urls import path

from . import views

app_name = "products"   # "sobrenome" das rotas deste app

urlpatterns = [
    path("", views.lista, name="lista"),
]