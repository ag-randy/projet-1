from django.urls import include, path 

urlpatterns = [
    path("", include("vitrine.urls")), 
]