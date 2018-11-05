from django.urls import path
from . import views 

urlpatterns = [
    path('', views.url_libros, name='url_libros'),
    path('lista_libros', views.listado_libros, name='listado_libros')
]