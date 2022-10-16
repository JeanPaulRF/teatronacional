from asyncore import read
from django.forms import ModelForm
from .models import *


class SigninForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'contrasena']



#create
class CreateAreaForm(ModelForm):
    class Meta:
        model = Area
        exclude = ['codigo', ]
        #fields = ['codigo', 'nombre', 'ubicacion', 'descripcion', 'dimensiones', 'listaElementos','imagen1', 'imagen2', 'imagen3']


class CreateElementoForm(ModelForm):
    class Meta:
        model = Elemento
        fields = ['nombre', 'ubicacion', 'descripcion', 'imagen1', 'imagen2', 'imagen3']


class CreateAgenteForm(ModelForm):
    class Meta:
        model = AgenteDeterioro
        fields = ['tDeterioro', 'nombre', 'descripcion']


class CreateEncargadoForm(ModelForm):
    class Meta:
        model = Encargado
        fields = ['tEncargado', 'nombre', 'telefono', 'email', 'identificacion']


class CreateInspeccionForm(ModelForm):
    class Meta:
        model = Inspeccion
        fields = ['fechaInicio', 'fechaFin', 'tResultado', 'tEstado', 'encargado', 'area', 'deterioro', 'comentario', 'pdf']


class CreateUserForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'contrasena', 'tUsuario']