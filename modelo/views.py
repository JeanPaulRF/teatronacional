from datetime import date
import datetime
import email
from unittest.loader import VALID_MODULE_NAME
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, get_user_model
from django.db.models import Q
from modelo.models import Usuario, AgenteDeterioro
from .forms import *
import os

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# from patterns.Snapshop import Snapshop



# Create your views here.

def temporal(request, id_):
    area = get_object_or_404(Area, id=id_)
    elementos = area.listaElementos.all()
    return render(request, 'preAsignacionTrabajo.html', { 'area' : area ,'elementos' : elementos })

def preAsignacionTrabajo(request,id_):
    area = get_object_or_404(Area, id=id_)
    elementos = area.listaElementos.all()
    return render(request, 'preAsignacionTrabajo.html', { 'area' : area ,'elementos' : elementos })

def asignacionTrabajoLista(request):
    areas = Area.objects.all()
    return render(request, 'asignacionTrabajo.html', { 'areas' : areas })

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
                    return redirect('listInspeccionesUser/{}'.format(usuario.id))
                elif usuario.tUsuario == 'DIRECCION':
                    return redirect('menuDireccion/')
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

#La informacion de una area y la lista de reportes de contenga el area <--- temporal/revisar
def readAreaReportes(request, idA_):
    area = get_object_or_404(Area, id=idA_)
    elementos = area.listaElementos.all()
    return render(request, 'areaInfoReportes.html', { 'area' : area ,'elementos' : elementos })

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
        return redirect('/menuAdmin/listaAreas/')
    else:
        return redirect('/menuAdmin/listaAreas/')




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

#Muestra los reportes de un elemento especifico  <--- funcion temporal
def readElementoReportes(request, idArea, idElemento):
    elemento = get_object_or_404(Elemento, id=idElemento)
    return render(request, 'elementoReportes.html', { 'elemento' : elemento, 'idArea': idArea })

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
            return render(request, 'editarElemento.html', {
                'elemento' : elemento,
                'form' : form,
                'error' : 'Elemento actualizado correctamente'
            })
        except ValueError:
            return render(request, 'editarElemento.html', {
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
            agente.save()

            return render(request, 'agregarAgenteDeterioro.html', {
                'form' : CreateAgenteForm,
                'error' : 'Agente creado correctamente'
            })

        except Exception as e:
            return render(request, 'agregarAgenteDeterioro.html', {
                'form' : CreateAgenteForm,
                'error' : 'Error al crear agente'
            })

    else:
        return render(request, 'agregarAgenteDeterioro.html', {
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
        return render(request, 'editarAgenteDeterioro.html', { 'agente' : agente , 'form' : form })
    else:
        try:
            agente = get_object_or_404(AgenteDeterioro, id=id_)
            form = CreateAgenteForm(request.POST, instance=agente)
            form.save()
            return render(request, 'editarAgenteDeterioro.html', {
                'agente' : agente,
                'form' : form,
                'error' : 'Agente actualizado correctamente'
            })
        except ValueError:
            return render(request, 'editarAgenteDeterioro.html', {
                'agente' : agente,
                'form' : form,
                'error' : 'Error al actualizar agente'
            })



def deleteAgente(request, id_):
    if request.method == 'POST':
        agente = get_object_or_404(AgenteDeterioro, id=id_)
        agente.delete()
        return redirect('/menuAdmin/verAgentesDeterioro/')
    else:
        return redirect('/menuAdmin/verAgentesDeterioro/')



#crud Encargado
def createEncargado(request):
    if request.method == 'POST':
        try:
            form = CreateEncargadoForm(request.POST)
            encargado = form.save(commit=False)
            encargado.user = request.user
            encargado.save()

            return render(request, 'agregarOperarios.html', {
                'form' : CreateEncargadoForm,
                'error' : 'Encargado creado correctamente'
            })

        except Exception as e:
            return render(request, 'agregarOperarios.html', {
                'form' : CreateEncargadoForm,
                'error' : 'Error al crear encargado'
            })

    else:
        return render(request, 'agregarOperarios.html', {
            'form' : CreateEncargadoForm
        })


#lista los agentes
def listEncargados(request):
    encargados = Encargado.objects.all()
    return render(request, 'listaEncargados.html', { 'encargados' : encargados })


def readEncargado(request, id_):
    encargado = get_object_or_404(Encargado, id=id_)
    return render(request, 'signin.html', { 'encargado' : encargado })


#lee un usuario especifico y actualizarlo
def updateEncargado(request, id_):
    if request.method == 'GET':
        encargado = get_object_or_404(Encargado, id=id_)
        form = CreateEncargadoForm(instance=encargado)
        return render(request, 'editarOperario.html', { 'encargado' : encargado , 'form' : form })
    else:
        try:
            encargado = get_object_or_404(Encargado, id=id_)
            form = CreateEncargadoForm(request.POST, instance=encargado)
            form.save()
            return render(request, 'editarOperario.html', {
                'encargado' : encargado,
                'form' : form,
                'error' : 'Encargado actualizado correctamente'
            })
        except ValueError:
            return render(request, 'editarOperario.html', {
                'encargado' : encargado,
                'form' : form,
                'error' : 'Error al actualizar encargado'
            })


def deleteEncargado(request, id_):
    encargado = get_object_or_404(Encargado, id=id_)
    if request.method == 'POST':
        encargado.delete()
        return redirect('/menuAdmin/listEncargados/')



#crud Inspeccion
def createInspeccion(request, id_):
    if request.method == 'POST':
        try:
            form = CreateInspeccionForm(request.POST)
            inspeccion = form.save(commit=False)
            inspeccion.save()

            return render(request, 'asignacion.html', {
                'form' : CreateInspeccionForm,
                'formato' : 'Formato fecha yyyy-mm-dd',
                'error' : 'Trabajo asignado correctamente'
            })

        except Exception as e:
            return render(request, 'asignacion.html', {
                'form' : CreateInspeccionForm,
                'formato' : 'Formato fecha yyyy-mm-dd',
                'error' : 'Error al asignar trabajo'
            })
    else:
        return render(request, 'asignacion.html', {
            'form' : CreateInspeccionForm,
            'formato' : 'Formato fecha yyyy-mm-dd',
        })




#lista inspecciones para admin
def listInspeccion(request):
    busqueda = request.GET.get("buscar")
    inspecciones = Inspeccion.objects.all()
    inspecciones1 = Inspeccion.objects.none()
    inspecciones2 = Inspeccion.objects.none()
    inspecciones3 = Inspeccion.objects.none()

    if busqueda:
        inspecciones = Inspeccion.objects.filter(
                Q(codigo = busqueda) | 
                Q(tResultado = busqueda) |
                Q(tEstado = busqueda)
            )

        try:
            area = Area.objects.get(nombre=busqueda)
            inspecciones1 = Inspeccion.objects.filter(area=area.id)
        except:
            pass

        try:
            encargado = Encargado.objects.get(nombre=busqueda)
            inspecciones2 = Inspeccion.objects.filter(encargado=encargado.id)
        except:
            pass

        try:
            inspecciones3 = Inspeccion.objects.filter(
                Q(fechaInicio = busqueda) |
                Q(fechaFin = busqueda)
            )
        except:
            pass

        inspecciones = inspecciones | inspecciones1 | inspecciones2 | inspecciones3

    return render(request, 'trabajosAsignadosAdmin.html', {'inspecciones' : inspecciones.distinct() })



def adminInspeccionInfo(request, id_):
    inspeccion = get_object_or_404(Inspeccion, id=id_)
    registros = inspeccion.registros.all()
    return render(request, 'adminInspeccionInfo.html', { 'inspeccion' : inspeccion ,
    'registros' : registros })


def readInspeccion(request, id_):
    inspeccion = get_object_or_404(Inspeccion, id=id_)
    return render(request, 'signin.html', { 'inspeccion' : inspeccion })


#lee un usuario especifico y actualizarlo
def updateInspeccion(request, id_):
    if request.method == 'GET':
        inspeccion = get_object_or_404(Inspeccion, id=id_)
        form = CreateInspeccionForm(instance=inspeccion)
        return render(request, 'ediatarTrabajoAsignadoAdmin.html', { 'inspeccion' : inspeccion , 'form' : form })
    else:
        try:
            inspeccion = get_object_or_404(Inspeccion, id=id_)
            form = CreateInspeccionForm(request.POST, instance=inspeccion)
            form.save()
            return render(request, 'ediatarTrabajoAsignadoAdmin.html', {
                'inspeccion' : inspeccion,
                'form' : form,
                'error' : 'Trabajo actualizado correctamente'
            })
        except ValueError:
            return render(request, 'ediatarTrabajoAsignadoAdmin.html', {
                'inspeccion' : inspeccion,
                'form' : form,
                'error' : 'Error al actualizar inspeccion'
            })



def deleteInspeccion(request, id_):
    inspeccion = get_object_or_404(Inspeccion, id=id_)
    if request.method == 'POST':
        inspeccion.delete()
        return redirect('/menuAdmin/listInspeccion/')



def listInspeccionesUser(request, id_):
    usuario = get_object_or_404(Usuario, id=id_)
    encargado = get_object_or_404(Encargado, email=usuario.email)
    user_inspecciones = Inspeccion.objects.filter(encargado=encargado.id)
    return render(request, 'trabajosAsignadosOperario.html', { 'inspecciones' : user_inspecciones })





def inspeccionInfo(request, id_):
    inspeccion = get_object_or_404(Inspeccion, id=id_)
    registros = inspeccion.registros.all()
    return render(request, 'inspeccionInfo.html', { 'inspeccion' : inspeccion ,'registros' : registros })


def editarInspeccion(request, idInspec):
    if request.method == 'POST':
        try:
            inspeccion = get_object_or_404(Inspeccion, id=idInspec)
            form = EditarInspeccionForm(request.POST, instance=inspeccion)
            inspeccion = form.save(commit=False)
            if len(request.FILES) != 0:
                if len(inspeccion.imagen) > 0:
                    os.remove(inspeccion.imagen.path)
                inspeccion.imagen = request.FILES['imagen']
            inspeccion.save()
            return render(request, 'editarInspeccion.html', {
                'inspeccion' : inspeccion,
                'form' : form,
                'error' : 'Inspeccion actualizada correctamente'
            })
        except ValueError:
            return render(request, 'editarInspeccion.html', {
                'inspeccion' : inspeccion,
                'form' : form,
                'error' : 'Error al actualizar inspeccion'
            })
    else:
        inspeccion = get_object_or_404(Inspeccion, id=idInspec)
        form = EditarInspeccionForm(instance=inspeccion)
        return render(request, 'editarInspeccion.html', { 'inspeccion' : inspeccion , 'form' : form })


def finalizarInspeccion(request, id_):
    if request.method == 'POST':
        inspeccion = get_object_or_404(Inspeccion, id=id_)
        inspeccion.completada = True
        inspeccion.tEstado = 'EJECUTADA'
        inspeccion.fechaFin = datetime.date.today()
        inspeccion.save()
        usuario = get_object_or_404(Usuario, email=inspeccion.encargado.email)
        encargado = get_object_or_404(Encargado, email=usuario.email)
        user_inspecciones = Inspeccion.objects.filter(encargado=encargado.id, completada=False)
        return redirect ('/listInspeccionesUser/{}'.format(usuario.id))

def agregarRegistro(request, idInspeccion):
    if request.method == 'GET':
        return render(request, 'agregarRegistro.html', {
            'form' : CreateRegistroForm,
        })
    else:
        try:
            form = CreateRegistroForm(request.POST, request.FILES)
            if form.is_valid():
                registro = form.save(commit=False)
                registro.save()
                inspeccion = Inspeccion.objects.get(id=idInspeccion)
                inspeccion.registros.add(registro)
                return render(request, 'agregarRegistro.html', {
                    'form' : CreateRegistroForm,
                    'error' : 'Elemento creado correctamente'
                })
            else:
                return render(request, 'agregarRegistro.html', {
                'form' : CreateRegistroForm,
                'error' : 'Error al crear registro form no valido'
            })
        except ValueError:
            return render(request, 'agregarRegistro.html', {
                'form' : CreateRegistroForm,
                'error' : 'Error al crear registro'
            })


def editarRegistro(request, idInspeccion):
    if request.method == 'POST':
        try:
            registro = get_object_or_404(RegistroInspeccion, id=idInspeccion)
            form = EditarInspeccionForm(request.POST, instance=inspeccion)
            inspeccion = form.save(commit=False)
            if len(request.FILES) != 0:
                if len(inspeccion.imagen) > 0:
                    os.remove(inspeccion.imagen.path)
                inspeccion.imagen = request.FILES['imagen']
            inspeccion.save()
            return render(request, 'editarInspeccion.html', {
                'inspeccion' : inspeccion,
                'form' : form,
                'error' : 'Inspeccion actualizada correctamente'
            })
        except ValueError:
            return render(request, 'editarInspeccion.html', {
                'inspeccion' : inspeccion,
                'form' : form,
                'error' : 'Error al actualizar inspeccion'
            })
    else:
        inspeccion = get_object_or_404(Inspeccion, id=idInspeccion)
        form = EditarInspeccionForm(instance=inspeccion)
        return render(request, 'editarInspeccion.html', { 'inspeccion' : inspeccion , 'form' : form })


def eliminarRegistro(request, id_):
    inspeccion = get_object_or_404(Inspeccion, id=id_)
    if request.method == 'POST':
        inspeccion.delete()
        return redirect('/menuAdmin/listInspeccion/')



def menuReportes(request):
    return render(request, 'reportes.html')


def areas_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Arial", 12)

    areas = Area.objects.all()
    lines = []

    #loop
    for area in areas:
        lines.append("area")
        lines.append("codigo: " + area.codigo)
        lines.append("nombre: " + area.nombre)
        lines.append("ubicacion: " + area.ubicacion)
        lines.append("descripcion: " + area.descripcion)
        lines.append("dimensiones: " + area.dimensiones)
        lines.append(" ")

        elementos = Elemento.objects.filter(area=area.id)
        for elemento in elementos:
            lines.append("elemento")
            lines.append("    codigo: " + elemento.codigo)
            lines.append("    nombre: " + elemento.nombre)
            lines.append("    ubicacion: " + elemento.ubicacion)
            lines.append("    descripcion: " + elemento.descripcion)
            lines.append(" ")

        lines.append(" ")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='Areas-elementos.pdf')



def agentes_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    agentes_ = AgenteDeterioro.objects.all()
    agentes = sorted(agentes_, key=lambda x: x.nombre)

    lines = []

    #loop
    lines.append("TIPO NATURAL")
    for agente in agentes:
        if agente.tDeterioro == "NATURAL":
            lines.append("    agente")
            lines.append("    nombre: " + agente.nombre)
            lines.append("    descripcion: " + agente.descripcion)
            lines.append(" ")

    lines.append("TIPO CIRCUNSTANCIAL")
    for agente in agentes:
        if agente.tDeterioro != "NATURAL":
            lines.append("    agente")
            lines.append("    nombre: " + agente.nombre)
            lines.append("    descripcion: " + agente.descripcion)
            lines.append(" ")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='Agentes.pdf')



def encargados_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    trabajos = Inspeccion.objects.all()
    encargados = Encargado.objects.all()
    conservaciones = []
    restauraciones = []
    inspecicones = []

    #loop
    for trabajo in trabajos:
        if trabajo.tResultado == "CONSERVACION":
            conservaciones.append("CONSERVACION")
            conservaciones.append(" ")
            conservaciones.append("    Encargado")
            conservaciones.append("    Nombre: " + trabajo.encargado.nombre)
            conservaciones.append("    Identificacion: " + trabajo.encargado.identificacion)
            conservaciones.append("    Tipo: " + trabajo.encargado.tEncargado)
            conservaciones.append("    Telefono: " + trabajo.encargado.telefono)
            conservaciones.append("    Email: " + trabajo.encargado.email)
        elif trabajo.tResultado == "RESTAURACION":
            restauraciones.append("RESTAURACION")
            restauraciones.append(" ")
            restauraciones.append("    Encargado")
            restauraciones.append("    Nombre: " + trabajo.encargado.nombre)
            restauraciones.append("    Identificacion: " + trabajo.encargado.identificacion)
            restauraciones.append("    Tipo: " + trabajo.encargado.tEncargado)
            restauraciones.append("    Telefono: " + trabajo.encargado.telefono)
            restauraciones.append("    Email: " + trabajo.encargado.email)
        elif trabajo.tResultado == "INSPECCION":
            inspecicones.append("INSPECCION")
            inspecicones.append(" ")
            inspecicones.append("    Encargado")
            inspecicones.append("    Nombre: " + trabajo.encargado.nombre)
            inspecicones.append("    Identificacion: " + trabajo.encargado.identificacion)
            inspecicones.append("    Tipo: " + trabajo.encargado.tEncargado)
            inspecicones.append("    Telefono: " + trabajo.encargado.telefono)
            inspecicones.append("    Email: " + trabajo.encargado.email)

    conservaciones.append(" ")
    conservaciones.append(" ")
    restauraciones.append(" ")
    restauraciones.append(" ")
    inspecicones.append(" ")
    inspecicones.append(" ")

    lines = []
    lines = conservaciones + restauraciones + inspecicones

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='Encargados.pdf')



def reporteInspeccion(request):
    return render(request, 'menuReporteInspeccion.html')


def reporteInspeccionFechas(request):
    if request.method == 'POST':
        fechaInicio = request.POST['fechaInicio']
        fechaFin = request.POST['fechaFin']
        inspecciones = Inspeccion.objects.filter(tResultado="INSPECCION")
        try:
            inspecciones=Inspeccion.objects.filter(fechaInicio__range=[fechaInicio, fechaFin], fechaFin__range=[fechaInicio, fechaFin])
            inspecciones = sorted(inspecciones, key=lambda x: x.fechaInicio)
        except:
            None
        return render(request, 'reporteInspeccionFecha.html', { 'form' : ReporteFechaForm, 'inspecciones': inspecciones})

    else:
        inspecciones = Inspeccion.objects.all()
        return render(request, 'reporteInspeccionFecha.html', { 'form' : ReporteFechaForm, 'inspecciones': inspecciones})


def reporteInspeccionFechasLista(request, fechaInicio, fechaFin):
    print(inspecciones)
    return render(request, 'reporteInspeccionFechaLista.html', { 'inspecciones' : inspecciones})



def reporteInspeccionCodigo(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        inspecciones = Inspeccion.objects.filter(codigo="INSPECCION")
        try:
            inspecciones=Inspeccion.objects.filter(codigo=codigo)
            inspecciones = sorted(inspecciones, key=lambda x: x.fechaInicio)
        except:
            None
        return render(request, 'reporteInspeccionCodigo.html', { 'form' : ReporteFechaForm, 'inspecciones': inspecciones})

    else:
        inspecciones = Inspeccion.objects.all()
        return render(request, 'reporteInspeccionCodigo.html', { 'form' : ReporteFechaForm, 'inspecciones': inspecciones})



def menuDireccion(request):
    return render(request, 'menuDireccion.html')