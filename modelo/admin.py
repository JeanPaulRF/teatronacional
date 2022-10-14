from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *

class FiltroCodigo(admin.ModelAdmin):
    readonly_fields= ('codigo',)

class FiltroParte(admin.ModelAdmin):
    list_display = ('nombre', 'codigo')
    readonly_fields= ('img_preview1', 'img_preview2', 'img_preview3', 'codigo')

class FiltroEncargado(admin.ModelAdmin):
    list_display = ('nombre', 'identificacion', 'email', 'tEncargado')

# Register your models here.
admin.site.register(Area, FiltroParte)
admin.site.register(Elemento, FiltroParte)
admin.site.register(AgenteDeterioro)
admin.site.register(Encargado, FiltroEncargado)
admin.site.register(Inspeccion, FiltroCodigo)
#admin.site.register(Usuario)

admin.site.unregister(User)
admin.site.unregister(Group)