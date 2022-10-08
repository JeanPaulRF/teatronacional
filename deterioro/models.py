from django.db import models

# Create your models here.
class AgenteDeterioro(models.Model):

    class TAgenteDeterioro(models.TextChoices):
        NATURAL = 'NATURAL', 'NATURAL'
        CIRCUNSTANCIAL = 'CIRCUNSTANCIAL', 'CIRCUNSTANCIAL'

    tDeterioro = models.CharField(max_length=2 , choices=TAgenteDeterioro.choices)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


