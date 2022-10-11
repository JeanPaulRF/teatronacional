from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *

class FiltroCodigo(admin.ModelAdmin):
    readonly_fields= ('codigo',)

class FiltroNombre(admin.ModelAdmin):
    list_display = ('nombre', 'codigo')
    readonly_fields= ('codigo',)

# Register your models here.
admin.site.register(Area, FiltroNombre)
admin.site.register(Elemento, FiltroNombre)
admin.site.register(AgenteDeterioro)
admin.site.register(Encargado)
admin.site.register(Inspeccion, FiltroCodigo)
#admin.site.register(Usuario)

admin.site.unregister(User)
admin.site.unregister(Group)