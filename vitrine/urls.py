from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("a_propos/", views.a_propos, name="a_propos"),
    path("projets/", views.projets, name="projets"),
    path("contact/", views.contact, name="contact"),
    path("services/", views.services, name="services"),
    path("services/<slug:slug>/", views.service_detail, name="service_detail"),
]