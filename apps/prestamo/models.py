from django.db import models
from apps.usuario.models import Usuario
from apps.ejemplar.models import Ejemplar
from apps.ejemplar.models import Libro

# Create your models here.

class Prestamo(models.Model):
    fecha_prestamo = models.DateField(max_length=50)
    fecha_devolucion = models.DateField(max_length=50)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ejemplar = models.ForeignKey(Ejemplar, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre