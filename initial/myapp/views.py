from django.shortcuts import render
from django.http import request ,HttpResponse,JsonResponse
from servicios.models import servicios
# Create your views here.

def home(request):
    return render(request,"myapp/home.html")

def tienda(request):
    return render(request,"myapp/tienda.html")

def contactos(request):
    return render(request,"myapp/contactos.html")


