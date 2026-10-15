from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("a_propos/", views.a_propos),                        # AJOUT
    path("services/", views.services),                        # AJOUT
    path("projets/", views.projets),                      # AJOUT
    path("contact/", views.contact),                          # AJOUT
]