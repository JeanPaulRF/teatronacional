from tkinter.messagebox import NO
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse, JsonResponse
from modelo.models import Usuario


# Create your views here.
def menuAdmin(request):
    return render(request, 'menuAdmin.html')

def autenticarUsuario(request):
    try:
        return get_object_or_404(Usuario, email=request.POST['username'])
    except Usuario.DoesNotExist:
        return None

def hola(email, password):
    print(email)

def signin(request):
    print(request.GET)
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        usuario = autenticarUsuario(request)

        if usuario is None:
            return render(request, 'signin.html', {
            'error' : 'Username o password son incorrectas'
        })

    return render(request, 'signin.html')





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