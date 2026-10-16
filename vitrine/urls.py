from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("a_propos/", views.a_propos, name="a_propos"),
    path("services/", views.services, name="services"),
    path("projets/", views.projets, name="projets"),
    path("contact/", views.contact, name="contact"),
]