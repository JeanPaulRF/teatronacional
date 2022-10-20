from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *


# Register your models here.
admin.site.register(User)
admin.site.register(Area)
admin.site.register(Elemento)
admin.site.register(AgenteDeterioro)
admin.site.register(Encargado)
admin.site.register(Trabajo)
admin.site.register(Usuario)
