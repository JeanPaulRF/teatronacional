from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse, JsonResponse
from modelo.models import Usuario
from .forms import SigninForm


# Create your views here.
def menuAdmin(request):
    return render(request, 'menuAdmin.html')


def hola(email, password):
    print(email)



def signin(request):
    if request.method == 'POST':
        try:
            usuario = Usuario.objects.get(email=request.POST['email'])

            if usuario.contrasena == request.POST['contrasena']:
                if usuario.tUsuario == 'ADMINISTRADOR':
                    return redirect('admin/')
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

def home(request):
    return render(request, 'home.html')


def signout(request):
    logout(request)
    return redirect('signin')	


def crearUsuario(request):
    user = Usuario(email=request.POST['email'], password=request.POST['password'])
    user.save()