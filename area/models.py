from django.db import models
from abc import ABC, abstractmethod

# Create your models here.
class Parte(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=8)
    ubicacion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        abstract = True


class Elemento(Parte):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Area(Parte):
    dimensiones = models.CharField(max_length=100)
    listaElementos = models.ManyToManyField(Elemento)

    def __str__(self):
        return self.name


