from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, get_user_model
from django.http import HttpResponse, JsonResponse
from modelo.models import Usuario
from .forms import *


# Create your views here.
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


# crudAreas.html
def createArea(request):
    if request.method == 'POST':
        try:
            form = CreateAreaForm(request.POST)
            area = form.save(commit=False)
            area.user = request.user
            area.save()

            return render(request, 'signin.html', {
                'form' : CreateAreaForm,
                'error' : 'Usuario creado correctamente'
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


def createElemento(request):
    if request.method == 'POST':
        try:
            form = CreateAreaForm(request.POST)
            area = form.save(commit=False)
            area.user = request.user
            area.save()

            return render(request, 'signin.html', {
                'form' : CreateAreaForm,
                'error' : 'Usuario creado correctamente'
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


# crudUsuarios.html

def createUser(request):
    if request.method == 'POST':
        try:
            user = get_user_model()
            user.objects.create_superuser(request.POST['email'], request.POST['email'], request.POST['contrasena'])
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