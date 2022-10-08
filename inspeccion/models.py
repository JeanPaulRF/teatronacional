from email.policy import default
from django.db import models
from area import models as area_models
from encargado import models as encargado_models
from deterioro import models as deterioro_models

# Create your models here.
class Inspeccion(models.Model):

    class TResultado(models.TextChoices):
        CONSERVACION = 'CONSERVACION', 'CONSERVACION'
        RESTAURACION = 'RESTAURACION', 'RESTAURACION'

    class TEstado(models.TextChoices):
        POR_SUCEDER = 'POR_SUCEDER', 'POR_SUCEDER'
        EN_EJECUCION = 'EN_EJECUCION', 'EN_EJECUCION'
        EJECUTADA = 'EJECUTADA', 'EJECUTADA'
        EJECUTADA_CON_RETRASO = 'EJECUTADA_CON_RETRASO', 'EJECUTADA_CON_RETRASO'
        RETRASADA = 'RETRASADA', 'RETRASADA'

    codigo = models.CharField(max_length=8)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    tResultado = models.CharField(max_length=2 , choices=TResultado.choices)
    tEstado = models.CharField(max_length=2 , choices=TEstado.choices, default=TEstado.POR_SUCEDER)
    encargado = models.OneToOneField(encargado_models.Encargado, on_delete=models.CASCADE)
    area = models.OneToOneField(area_models.Area, on_delete=models.CASCADE)
    deterio = models.OneToOneField(deterioro_models.AgenteDeterioro, on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo