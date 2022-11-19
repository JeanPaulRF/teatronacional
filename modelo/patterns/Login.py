from modelo.patterns.Proxy import Proxy
from django.db.models import Q
from modelo.models import Usuario, AgenteDeterioro
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.shortcuts import render, redirect
from modelo.forms import SigninForm

class Login(Proxy):


    def __init__(self):
        pass

    def login(self, email, password, request):
        try:
            usuario = Usuario.objects.get(email=email)

            if usuario.contrasena == password:
                if usuario.tUsuario == 'ADMINISTRADOR':
                    return redirect('menuAdmin/')
                elif usuario.tUsuario == 'SUPERUSUARIO':
                    return redirect('listaUsuarios/')
                elif usuario.tUsuario == 'OPERATIVO':
                    return redirect('listInspeccionesUser/{}'.format(usuario.id))
                elif usuario.tUsuario == 'DIRECCION':
                    return redirect('menuDireccion/')
            else:
                return render(request, 'signin.html', {
                    'form' : SigninForm,
                    'error' : 'Contraseña incorrecta'
                })
        except Usuario.DoesNotExist:
            return render(request, 'signin.html', {
                'form' : SigninForm,
                'error' : 'El usuario no existe'
            })
