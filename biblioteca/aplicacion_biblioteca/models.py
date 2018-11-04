from django.db import models
from django.utils import timezone

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    categoria = models.CharField(max_length=200)
    descripcion = models.TextField()
    date_create = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank = True, null=True)


    def publicacion(self):
        self.fecha_publicacion= timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
