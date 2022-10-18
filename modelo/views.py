import email
from unittest.loader import VALID_MODULE_NAME
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, get_user_model
from django.http import HttpResponse, JsonResponse
from modelo.models import Usuario
from .forms import *
import os


# Create your views here.
def asignacionTrabajo(request):
    areas = Area.objects.all()
    return render(request, 'asignacionTrabajo.html', { 'areas' : areas })

def agregarElemento(request):
    return render(request, 'agregarElemento.html')

def agregarArea(request):
    return render(request, 'agregarArea.html')

def elementoInfoAdmin(request):
    return render(request, 'elementoInfoAdmin.html')

def areasInfoAdmin(request):
    return render(request, 'areasInfoAdmin.html')

def areasLista(request):
    areas = Area.objects.all()
    print(areas)
    return render(request, 'listaAreas.html', { 'areas' : areas })
    # return render(request, 'listaAreas.html')
#''''''''''''''''''''''''''''''''''''''
def menuAdmin(request):
    return render(request, 'menuAdmin.html')





def signin(request):
    if request.method == 'POST':
        try:
            usuario = Usuario.objects.get(email=request.POST['email'])

            if usuario.contrasena == request.POST['contrasena']:
                if usuario.tUsuario == 'ADMINISTRADOR':
                    return redirect('menuAdmin/')
                elif usuario.tUsuario == 'SUPERUSUARIO':
                    return redirect('listaUsuarios/')
                elif usuario.tUsuario == 'OPERATIVO':
                    return redirect('listaInspeccionesUser/{}'.format(usuario.id))
            else:
                return render(request, 'signin.html', {
                    'form' : SigninForm,
                    'error' : 'Contraseña incorrecta'
                })

        except Exception as e:
            return render(request, 'signin.html', {
                'form' : SigninForm,
                'error' : 'El usuario no existe'
            })

    else:
        return render(request, 'signin.html', {
            'form' : SigninForm
        })



def signup(request):
    return render(request, 'signup.html', {
        'form': UserCreationForm
    })

def areasyelementos(request):
    return redirect('')

def home(request):
    return render(request, 'home.html')
    
def agentesdeterioro(request):
    return redirect('')

def inspecciones(request):
    return redirect('')


def signout(request):
    return redirect('')	

def usuarios(request):
    return redirect('')

def encargados(request):
    return redirect('')


# crud Area
def createArea(request):
    if request.method == 'GET':
        return render(request, 'agregarArea.html', {
            'form' : CreateAreaForm,
        })
    else:
        try:
            form = CreateAreaForm(request.POST, request.FILES)
            if form.is_valid():
                area = form.save(commit=False)
                print(area.imagen1)
                area.save()
                return render(request, 'agregarArea.html', {
                    'form' : CreateAreaForm,
                    'error' : 'Area creada correctamente'
                })
            else:
                return render(request, 'agregarArea.html', {
                'form' : CreateAreaForm,
                'error' : 'Error al crear area form no valido'
            })
        except ValueError:
            return render(request, 'agregarArea.html', {
                'form' : CreateAreaForm,
                'error' : 'Error al crear area'
            })
       


#lista las areas
def listAreas(request):
    areas = Area.objects.all()
    return render(request, 'listaAreas.html', { 'areas' : areas })


def readArea(request, id_):
    area = get_object_or_404(Area, id=id_)
    elementos = area.listaElementos.all()
    return render(request, 'areasInfoAdmin.html', { 'area' : area ,'elementos' : elementos })


#lee un area especifica y actualizarla
def updateArea(request, id_):
    if request.method == 'GET':
        area = get_object_or_404(Area, id=id_)
        form = CreateAreaForm(instance=area)
        return render(request, 'editarAreaAdmin.html', { 'area' : area , 'form' : form })
    else:
        try:
            area = get_object_or_404(Area, id=id_)
            form = CreateAreaForm(request.POST, instance=area)
            area = form.save(commit=False)
            if len(request.FILES) != 0:
                if len(area.imagen1) > 0:
                    os.remove(area.imagen1.path)
                area.imagen1 = request.FILES['imagen1']

                if len(area.imagen2) > 0:
                    os.remove(area.imagen2.path)
                area.imagen2 = request.FILES['imagen2']

                if len(area.imagen3) > 0:
                    os.remove(area.imagen3.path)
            area.save()
            return render(request, 'editarAreaAdmin.html', {
                'area' : area,
                'form' : form,
                'error' : 'Area actualizada correctamente'
            })
        except ValueError:
            return render(request, 'editarAreaAdmin.html', {
                'area' : area,
                'form' : form,
                'error' : 'Error al actualizar area'
            })


def deleteArea(request, id_):
    if request.method == 'POST':
        area = get_object_or_404(Area, id=id_)
        area.delete()
        return render(request, 'listaAreas.html')
    else:
        return render(request, 'listaAreas.html')




# crud Elemento

def createElemento(request, idArea):
    if request.method == 'GET':
        return render(request, 'agregarElemento.html', {
            'form' : CreateElementoForm,
        })
    else:
        try:
            form = CreateElementoForm(request.POST, request.FILES)
            if form.is_valid():
                elemento = form.save(commit=False)
                elemento.save()
                area = Area.objects.get(id=idArea)
                area.listaElementos.add(elemento)
                return render(request, 'agregarElemento.html', {
                    'form' : CreateElementoForm,
                    'error' : 'Elemento creado correctamente'
                })
            else:
                return render(request, 'agregarElemento.html', {
                'form' : CreateElementoForm,
                'error' : 'Error al crear elemento form no valido'
            })
        except ValueError:
            return render(request, 'agregarElemento.html', {
                'form' : CreateElementoForm,
                'error' : 'Error al crear elemento'
            })


#lista las areas
def listElementos(request, idArea):
    area = get_object_or_404(Area, id=idArea)
    elementos = area.listaElementos.objects.all()
    return render(request, 'signin.html', { 'elementos' : elementos })


def readElemento(request, idArea, idElemento):
    elemento = get_object_or_404(Elemento, id=idElemento)
    return render(request, 'elementoInfoAdmin.html', { 'elemento' : elemento, 'idArea': idArea })


#lee un area especifica y actualizarla
def updateElemento(request, idArea, idElemento):
    if request.method == 'GET':
        elemento = get_object_or_404(Elemento, id=idElemento)
        form = CreateElementoForm(instance=elemento)
        return render(request, 'editarElemento.html', { 'elemento' : elemento , 'form' : form })
    else:
        try:
            elemento = get_object_or_404(Elemento, id=idElemento)
            form = CreateElementoForm(request.POST, instance=elemento)
            form.save()
            return redirect('')
        except ValueError:
            return render(request, 'signin.html', {
                'elemento' : elemento,
                'form' : form,
                'error' : 'Error al actualizar elemento'
            })


def deleteElemento(request, idArea, idElemento):
    if request.method == 'POST':
        elemento = get_object_or_404(Elemento, id=idElemento)
        elemento.delete()
        return redirect('/menuAdmin/listaAreas/areasInfoAdmin/{}'.format(idArea))
    else:
        return redirect('/menuAdmin/listaAreas/areasInfoAdmin/{}'.format(idArea))



def createArea(request):
    if request.method == 'GET':
        return render(request, 'agregarArea.html', {
            'form' : CreateAreaForm,
        })
    else:
        try:
            form = CreateAreaForm(request.POST, request.FILES)
            if form.is_valid():
                area = form.save(commit=False)
                area.save()
                return render(request, 'agregarArea.html', {
                    'form' : CreateAreaForm,
                    'error' : 'Area creada correctamente'
                })
            else:
                return render(request, 'agregarArea.html', {
                'form' : CreateAreaForm,
                'error' : 'Error al crear area form no valido'
            })
        except ValueError:
            return render(request, 'agregarArea.html', {
                'form' : CreateAreaForm,
                'error' : 'Error al crear area'
            })


# crud Usuarios

def createUser(request):
    if request.method == 'GET':
        return render(request, 'agregarUsuario.html', {
            'form' : CreateUserForm
        })
    else:
        try:
            form = CreateUserForm(request.POST)
            if form.is_valid():
                usuario = form.save(commit=False)
                usuario.user = request.user
                usuario.save()
            return render(request, 'agregarUsuario.html', {
                'form' : CreateUserForm,
                'error' : 'Usuario creado correctamente'
            })

        except ValueError:
            return render(request, 'agregarUsuario.html', {
                'form' : CreateUserForm,
                'error' : 'Error al crear usuario'
            })

    

#lista los usuarios
def listUsers(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listaUsuarios.html', { 'usuarios' : usuarios })


def readUser(request, id_):
    usuario = get_object_or_404(Usuario, id=id_)
    return render(request, 'signin.html', { 'usuario' : usuario })


#lee un usuario especifico y actualizarlo
def updateUser(request, id_):
    if request.method == 'GET':
        usuario = get_object_or_404(Usuario, id=id_)
        form = CreateUserForm(instance=usuario)
        return render(request, 'editarUsuario.html', { 'usuario' : usuario , 'form' : form })
    else:
        try:
            usuario = get_object_or_404(Usuario, id=id_)
            form = CreateUserForm(request.POST, instance=usuario)
            form.save()
            return render(request, 'editarUsuario.html', { 
                'usuario' : usuario , 
                'form' : form ,
                'error' : 'Usuario actualizado correctamente'
            })
        except ValueError:
            return render(request, 'editarUsuario.html', {
                'usuario' : usuario,
                'form' : form,
                'error' : 'Error al actualizar usuario'
            })




def updateArea(request, id_):
    if request.method == 'GET':
        area = get_object_or_404(Area, id=id_)
        form = CreateAreaForm(instance=area)
        return render(request, 'editarAreaAdmin.html', { 'area' : area , 'form' : form })
    else:
        try:
            area = get_object_or_404(Area, id=id_)
            form = CreateAreaForm(request.POST, instance=area)
            area = form.save(commit=False)
            if len(request.FILES) != 0:
                if len(area.imagen1) > 0:
                    os.remove(area.imagen1.path)
                area.imagen1 = request.FILES['imagen1']

                if len(area.imagen2) > 0:
                    os.remove(area.imagen2.path)
                area.imagen2 = request.FILES['imagen2']

                if len(area.imagen3) > 0:
                    os.remove(area.imagen3.path)
            area.save()
            return render(request, 'editarAreaAdmin.html', {
                'area' : area,
                'form' : form,
                'error' : 'Area actualizada correctamente'
            })
        except ValueError:
            return render(request, 'editarAreaAdmin.html', {
                'area' : area,
                'form' : form,
                'error' : 'Error al actualizar area'
            })




def deleteUser(request, id_):
    if request.method == 'POST':
        usuario = get_object_or_404(Usuario, id=id_)
        usuario.delete()
        return redirect('/listaUsuarios/')
    else:
        return redirect('/listaUsuarios/')




# crud AgenteDeterioro

def createAgente(request):
    if request.method == 'POST':
        try:
            form = CreateAgenteForm(request.POST)
            agente = form.save(commit=False)
            agente.user = request.user
            agente.save()

            return render(request, 'signin.html', {
                'form' : CreateAgenteForm,
                'error' : 'Agente creado correctamente'
            })

        except Exception as e:
            return render(request, 'signin.html', {
                'form' : CreateAgenteForm,
                'error' : 'Error al crear agente'
            })

    else:
        return render(request, 'signin.html', {
            'form' : CreateAgenteForm
        })


#lista los agentes
def verAgentesDeterioro(request):
    agentes = AgenteDeterioro.objects.all()
    return render(request, 'verAgentesDeterioro.html', { 'agentes' : agentes })


def readAgente(request, id_):
    agente = get_object_or_404(AgenteDeterioro, id=id_)
    return render(request, 'signin.html', { 'agente' : agente })


#lee un usuario especifico y actualizarlo
def updateAgente(request, id_):
    if request.method == 'GET':
        agente = get_object_or_404(AgenteDeterioro, id=id_)
        form = CreateAgenteForm(instance=agente)
        return render(request, 'signin.html', { 'agente' : agente , 'form' : form })
    else:
        try:
            agente = get_object_or_404(AgenteDeterioro, id=id_)
            form = CreateAgenteForm(request.POST, instance=agente)
            form.save()
            return redirect('')
        except ValueError:
            return render(request, 'signin.html', {
                'agente' : agente,
                'form' : form,
                'error' : 'Error al actualizar agente'
            })


def deleteAgente(request, id_):
    agente = get_object_or_404(AgenteDeterioro, id=id_)
    if request.method == 'POST':
        agente.delete()
        return redirect('')



#crud Encargado
def createEncargado(request):
    if request.method == 'POST':
        try:
            form = CreateEncargadoForm(request.POST)
            encargado = form.save(commit=False)
            encargado.user = request.user
            encargado.save()

            return render(request, 'signin.html', {
                'form' : CreateEncargadoForm,
                'error' : 'Encargado creado correctamente'
            })

        except Exception as e:
            return render(request, 'signin.html', {
                'form' : CreateEncargadoForm,
                'error' : 'Error al crear encargado'
            })

    else:
        return render(request, 'signin.html', {
            'form' : CreateEncargadoForm
        })


#lista los agentes
def listEncargados(request):
    encargados = Encargado.objects.all()
    return render(request, 'signin.html', { 'encargados' : encargados })


def readEncargado(request, id_):
    encargado = get_object_or_404(Encargado, id=id_)
    return render(request, 'signin.html', { 'encargado' : encargado })


#lee un usuario especifico y actualizarlo
def updateEncargado(request, id_):
    if request.method == 'GET':
        encargado = get_object_or_404(Encargado, id=id_)
        form = CreateEncargadoForm(instance=encargado)
        return render(request, 'signin.html', { 'encargado' : encargado , 'form' : form })
    else:
        try:
            encargado = get_object_or_404(Encargado, id=id_)
            form = CreateEncargadoForm(request.POST, instance=encargado)
            form.save()
            return redirect('')
        except ValueError:
            return render(request, 'signin.html', {
                'encargado' : encargado,
                'form' : form,
                'error' : 'Error al actualizar encargado'
            })


def deleteEncargado(request, id_):
    encargado = get_object_or_404(Encargado, id=id_)
    if request.method == 'POST':
        encargado.delete()
        return redirect('')



#crud Inspeccion
def createInspeccion(request):
    if request.method == 'POST':
        try:
            form = CreateInspeccionForm(request.POST)
            inspeccion = form.save(commit=False)
            inspeccion.user = request.user
            inspeccion.save()

            return render(request, 'signin.html', {
                'form' : CreateInspeccionForm,
                'error' : 'Inspeccion creada correctamente'
            })

        except Exception as e:
            return render(request, 'signin.html', {
                'form' : CreateInspeccionForm,
                'error' : 'Error al crear inspeccion'
            })

    else:
        return render(request, 'signin.html', {
            'form' : CreateInspeccionForm
        })


#lista los agentes
def listInspeccion(request):
    inspecciones = Inspeccion.objects.all()
    return render(request, 'signin.html', { 'inspecciones' : inspecciones })


def readInspeccion(request, id_):
    inspeccion = get_object_or_404(Inspeccion, id=id_)
    return render(request, 'signin.html', { 'inspeccion' : inspeccion })


#lee un usuario especifico y actualizarlo
def updateInspeccion(request, id_):
    if request.method == 'GET':
        inspeccion = get_object_or_404(Inspeccion, id=id_)
        form = CreateInspeccionForm(instance=inspeccion)
        return render(request, 'signin.html', { 'inspeccion' : inspeccion , 'form' : form })
    else:
        try:
            inspeccion = get_object_or_404(Inspeccion, id=id_)
            form = CreateInspeccionForm(request.POST, instance=inspeccion)
            form.save()
            return redirect('')
        except ValueError:
            return render(request, 'signin.html', {
                'inspeccion' : inspeccion,
                'form' : form,
                'error' : 'Error al actualizar inspeccion'
            })


def deleteInspecion(request, id_):
    inspeccion = get_object_or_404(Inspeccion, id=id_)
    if request.method == 'POST':
        inspeccion.delete()
        return redirect('')




def listInspeccionesUser(request, id_):
    usuario = get_object_or_404(Usuario, id=id_)
    encargado = get_object_or_404(Encargado, email=usuario.email)
    user_inspecciones = Inspeccion.objects.filter(encargado=encargado)
    inspecciones = Inspeccion.objects.exclude(pk__in=user_inspecciones)
    print(inspecciones)
    return render(request, 'listaInspeccionesUser.html', { 'inspecciones' : inspecciones })
