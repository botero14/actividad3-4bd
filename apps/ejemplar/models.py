from django.db import models
from apps.libro.models import Libro

# Create your models here.

class Ejemplar(models.Model):
    localizacion = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre