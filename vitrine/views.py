from django.http import Http404, HttpResponse  # MODIFIÉ
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def a_propos(request):
    return render(request, "a_propos.html")

def services(request):  
    return render(request, "services.html") 

def projets(request):
    return render(request, "projets.html")

def contact(request):
    return render(request, "contact.html")  