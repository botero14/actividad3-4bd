from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    numero_paginas = models.IntegerField(max_length=50)



    def __str__(self):
        return self.nombre