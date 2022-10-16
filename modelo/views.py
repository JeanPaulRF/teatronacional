from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, get_user_model
from django.http import HttpResponse, JsonResponse
from modelo.models import Usuario
from .forms import *


# Create your views here.
def agregarElemento(request):
    return render(request, 'agregarElemento.html')

def agregarArea(request):
    return render(request, 'agregarArea.html')

def elementoInfoAdmin(request):
    return render(request, 'elementoInfoAdmin.html')

def areasInfoAdmin(request):
    return render(request, 'areasInfoAdmin.html')

def areasLista(request):
    return render(request, 'listaAreas.html')

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
                    return redirect('home/')
                elif usuario.tUsuario == 'OPERATIVO':
                    return redirect('home/')
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
    if request.method == 'POST':
        try:
            form = CreateAreaForm(request.POST)
            area = form.save(commit=False)
            area.user = request.user
            area.save()

            return render(request, 'signin.html', {
                'form' : CreateAreaForm,
                'error' : 'Area creada correctamente'
            })

        except Exception as e:
            return render(request, 'signin.html', {
                'form' : CreateAreaForm,
                'error' : 'Error al crear area'
            })

    else:
        return render(request, 'signin.html', {
            'form' : CreateAreaForm
        })


#lista las areas
def listAreas(request):
    areas = Area.objects.all()
    return render(request, 'signin.html', { 'areas' : areas })


#lee un area especifica y actualizarla
def readArea(request, id_):
    if request.method == 'GET':
        area = get_object_or_404(Area, id=id_)
        form = CreateAreaForm(instance=area)
        return render(request, 'signin.html', { 'area' : area , 'form' : form })
    else:
        try:
            area = get_object_or_404(Area, id=id_)
            form = CreateAreaForm(request.POST, instance=area)
            form.save()
            return redirect('')
        except ValueError:
            return render(request, 'signin.html', {
                'area' : area,
                'form' : form,
                'error' : 'Error al actualizar area'
            })


def deleteArea(request, id_):
    area = get_object_or_404(Area, id=id_)
    if request.method == 'POST':
        area.delete()
        return redirect('')




# crud Elemento

def createElemento(request):
    if request.method == 'POST':
        try:
            form = CreateElementoForm(request.POST)
            elemento = form.save(commit=False)
            elemento.user = request.user
            elemento.save()

            return render(request, 'signin.html', {
                'form' : CreateElementoForm,
                'error' : 'Elemento creado correctamente'
            })

        except Exception as e:
            return render(request, 'signin.html', {
                'form' : CreateElementoForm,
                'error' : 'Error al crear elemento'
            })

    else:
        return render(request, 'signin.html', {
            'form' : CreateElementoForm
        })


#lista las areas
def listElementos(request):
    elementos = Elemento.objects.all()
    return render(request, 'signin.html', { 'elementos' : elementos })


#lee un area especifica y actualizarla
def readElemento(request, id_):
    if request.method == 'GET':
        elemento = get_object_or_404(Elemento, id=id_)
        form = CreateElementoForm(instance=elemento)
        return render(request, 'signin.html', { 'elemento' : elemento , 'form' : form })
    else:
        try:
            elemento = get_object_or_404(Elemento, id=id_)
            form = CreateElementoForm(request.POST, instance=elemento)
            form.save()
            return redirect('')
        except ValueError:
            return render(request, 'signin.html', {
                'elemento' : elemento,
                'form' : form,
                'error' : 'Error al actualizar elemento'
            })


def deleteElemento(request, id_):
    elemento = get_object_or_404(Elemento, id=id_)
    if request.method == 'POST':
        elemento.delete()
        return redirect('')



# crud Usuarios

def createUser(request):
    if request.method == 'POST':
        try:
            form = CreateUserForm(request.POST)
            usuario = form.save(commit=False)
            usuario.user = request.user
            usuario.save()

            return render(request, 'signin.html', {
                'form' : CreateUserForm,
                'error' : 'Usuario creado correctamente'
            })

        except Exception as e:
            return render(request, 'signin.html', {
                'form' : CreateUserForm,
                'error' : 'Error al crear usuario'
            })

    else:
        return render(request, 'signin.html', {
            'form' : CreateUserForm
        })

#lista los usuarios
def listUsers(request):
    usuarios = Usuario.objects.all()
    return render(request, 'signin.html', { 'usuarios' : usuarios })


#lee un usuario especifico y actualizarlo
def readUser(request, id_):
    if request.method == 'GET':
        usuario = get_object_or_404(Usuario, id=id_)
        form = CreateUserForm(instance=usuario)
        return render(request, 'signin.html', { 'usuario' : usuario , 'form' : form })
    else:
        try:
            usuario = get_object_or_404(Usuario, id=id_)
            form = CreateUserForm(request.POST, instance=usuario)
            form.save()
            return redirect('')
        except ValueError:
            return render(request, 'signin.html', {
                'usuario' : usuario,
                'form' : form,
                'error' : 'Error al actualizar usuario'
            })


def deleteUser(request, id_):
    usuario = get_object_or_404(Usuario, id=id_)
    if request.method == 'POST':
        usuario.delete()
        return redirect('')




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
def listAgentes(request):
    agentes = AgenteDeterioro.objects.all()
    return render(request, 'signin.html', { 'agentes' : agentes })


#lee un usuario especifico y actualizarlo
def readAgente(request, id_):
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


#lee un usuario especifico y actualizarlo
def readAgente(request, id_):
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


#lee un usuario especifico y actualizarlo
def readAgente(request, id_):
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