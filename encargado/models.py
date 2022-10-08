from email.policy import default
from django.db import models

# Create your models here.
class Encargado(models.Model):

    class TEncargado(models.TextChoices):
        INTERNO = 'INTERNO', 'INTERNO'
        EXTERNO = 'EXTERNO', 'EXTERNO'
        SUBCONTRATADO = 'SUBCONTRATADO', 'SUBCONTRATADO'

    tEncargado = models.CharField(max_length=2 , choices=TEncargado.choices)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre