from django.shortcuts import render
from .models import Libro

# Create your views here.

def url_libros(request): 
    libros = Libro.objects.all()
    return render (request, "libros/libros_list_home.html", {'libros':libros})


def listado_libros(request):
    libros = Libro.objects.all()
    return render (request, "libros/lista_libros.html", {'libros':libros})