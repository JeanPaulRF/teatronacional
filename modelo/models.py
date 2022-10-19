from contextlib import nullcontext
from enum import unique
from django.db import models
from django.utils.html import mark_safe
import uuid



# Create your models here.


#areas
class Parte(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=8, default=uuid.uuid1, editable=False, unique=True, )
    ubicacion = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen1 = models.ImageField(null=True, blank=True, upload_to='images/')
    imagen2 = models.ImageField(null=True, blank=True, upload_to='images/')
    imagen3 = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.nombre

    class Meta:
        abstract = True
    


class Elemento(Parte):

    def __str__(self):
        return self.nombre


class Area(Parte):
    dimensiones = models.CharField(max_length=100)
    listaElementos = models.ManyToManyField(Elemento, blank=True, null=True)

    def __str__(self):
        return self.nombre



#encargados
class Encargado(models.Model):

    class TEncargado(models.TextChoices):
        INTERNO = 'INTERNO', 'INTERNO'
        EXTERNO = 'EXTERNO', 'EXTERNO'
        SUBCONTRATADO = 'SUBCONTRATADO', 'SUBCONTRATADO'

    tEncargado = models.CharField(max_length=25 , choices=TEncargado.choices)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


#usuarios
class Usuario(models.Model):

    class TUsuario(models.TextChoices):
        ADMINISTRADOR = 'ADMINISTRADOR', 'ADMINISTRADOR'
        SUPERUSUARIO = 'SUPERUSUARIO', 'SUPERUSUARIO'
        OPERATIVO = 'OPERATIVO', 'OPERATIVO'

    tUsuario = models.CharField(max_length=25 , choices=TUsuario.choices, default=TUsuario.OPERATIVO)
    contrasena = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.email


#deterioros
class AgenteDeterioro(models.Model):

    class TAgenteDeterioro(models.TextChoices):
        NATURAL = 'NATURAL', 'NATURAL'
        CIRCUNSTANCIAL = 'CIRCUNSTANCIAL', 'CIRCUNSTANCIAL'

    tDeterioro = models.CharField(max_length=25 , choices=TAgenteDeterioro.choices)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


#inspecciones
class Trabajo(models.Model):

    class TResultado(models.TextChoices):
        CONSERVACION = 'CONSERVACION', 'CONSERVACION'
        RESTAURACION = 'RESTAURACION', 'RESTAURACION'
        INSPECCION = 'INSPECCION', 'INSPECCION'

    class TEstado(models.TextChoices):
        POR_SUCEDER = 'POR_SUCEDER', 'POR_SUCEDER'
        EN_EJECUCION = 'EN_EJECUCION', 'EN_EJECUCION'
        EJECUTADA = 'EJECUTADA', 'EJECUTADA'
        EJECUTADA_CON_RETRASO = 'EJECUTADA_CON_RETRASO', 'EJECUTADA_CON_RETRASO'
        RETRASADA = 'RETRASADA', 'RETRASADA'

    codigo = models.CharField(max_length=8, default=uuid.uuid1, editable=False, unique=True, )
    fechaInicio = models.DateField(null=False)
    fechaFin = models.DateField(null=False)
    tResultado = models.CharField(max_length=25 , choices=TResultado.choices)
    tEstado = models.CharField(max_length=25 , choices=TEstado.choices, default=TEstado.POR_SUCEDER)
    encargado = models.ForeignKey(Encargado, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    deterioro = models.ForeignKey(AgenteDeterioro, on_delete=models.CASCADE)
    comentario = models.TextField(default='')
    pdf = models.FileField(upload_to='pdf/', blank=True, null=True)

    def __str__(self):
        return self.tEstado