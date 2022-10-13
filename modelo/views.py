from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from modelo.models import Usuario


# Create your views here.
def autenticarUsuario(request):
    try:
        return get_object_or_404(Usuario, email=request.POST['username'])
    except Usuario.DoesNotExist:
        return None

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form' : AuthenticationForm
        })
    else:
        usuario = autenticarUsuario(request)

        if usuario is None:
            return render(request, 'signin.html', {
            'form' : AuthenticationForm,
            'error' : 'Username o password son incorrectas'
        })

    return render(request, 'signin.html', {
            'form' : AuthenticationForm
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