from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return HttpResponse("<h1>Prueba 1 :D</h1><h2>Portada</h2>")
