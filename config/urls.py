from django.urls import include, path  # MODIFIÉ

urlpatterns = [
    path("", include("vitrine.urls")),  # AJOUT
]