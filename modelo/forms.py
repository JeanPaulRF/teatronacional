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
        fields = ['codigo', 'nombre', 'ubicacion', 'descripcion', 'dimensiones', 'listaElementos','imagen1', 'imagen2', 'imagen3']


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
        fields = ['fechaInicio', 'fechaFin', 'encargado', 'area']


class EditarInspeccionForm(ModelForm):
    class Meta:
        model = Inspeccion
        fields = ['tResultado', 'tEstado', 'comentario', 'pdf']


class BuscarInspeccionForm(ModelForm):
    class Meta:
        model = Inspeccion
        fields = ['tEstado', 'fechaInicio', 'fechaFin', 'encargado', 'area', 'tResultado']


class CreateRegistroForm(ModelForm):
    class Meta:
        model = RegistroInspeccion
        fields = ['imagen', 'deterioro', 'observacion', 'recomendacion']


class CreateUserForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'contrasena', 'tUsuario']


class ReporteFechaForm(ModelForm):
    class Meta:
        model = Inspeccion
        fields = ['fechaInicio', 'fechaFin']