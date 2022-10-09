from django.contrib import admin
from .models import Area, Elemento, AgenteDeterioro, Encargado, Inspeccion, Usuario

# Register your models here.
admin.site.register(Area, Elemento, AgenteDeterioro, Encargado, Inspeccion), Usuario