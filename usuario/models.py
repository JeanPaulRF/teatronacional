from email.policy import default
from django.db import models

# Create your models here.
class Usuario(models.Model):

    class TUsuario(models.TextChoices):
        ADMINISTRADOR = 'ADMINISTRADOR', 'ADMINISTRADOR'
        SUPERUSUARIO = 'SUPERUSUARIO', 'SUPERUSUARIO'
        OPERATIVO = 'OPERATIVO', 'OPERATIVO'

    tUsuario = models.CharField(max_length=2 , choices=TUsuario.choices, default=TUsuario.OPERATIVO)
    contrasena = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre