from django.shortcuts import render, get_object_or_404
from .models import Libro

# Create your views here.

def url_libros(request): 
    libros = Libro.objects.all()
    return render (request, "libros/libros_list_home.html", {'libros':libros})


def listado_libros(request):
    libros = Libro.objects.all()
    return render (request, "libros/lista_libros.html", {'libros':libros})

def detalle(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'libros/detalle.html', {'libro': libro})