from django.shortcuts import render
from .models import services

# Create your views here.
def Services(request):
    servicios = services.objects.all()
    return render (request,"services/services.html",{'Services':servicios})
