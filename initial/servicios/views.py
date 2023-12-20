from django.shortcuts import render
from .models import servicios
from django.http import request ,JsonResponse,HttpResponse



def servicios(request):
    
   
    return render(request,"servicios/servicios.html")
