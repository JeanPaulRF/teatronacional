"""teatro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from modelo import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signin, name='signin'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='signout'),
    path('listaUsuarios/', views.listUsers, name='listUsuarios'),
    path('listaInspeccionesUser/<int:id_>/', views.listInspeccionesUser, name='listInspeccionesUser'),
    path('listaUsuarios/agregarUsuario/', views.createUser, name='agregarUsuario'),
    path('listaUsuarios/updateUsuario/<int:id_>', views.updateUser, name='updateUsuario'),
    path('listaUsuarios/deleteUsuario/<int:id_>', views.deleteUser, name='deleteUsuario'),
    path('menuAdmin/', views.menuAdmin, name='menuAdmin'),
    path('menuAdmin/listaAreas/', views.listAreas, name='listAreas'),
    path('menuAdmin/listaAreas/agregarArea/', views.createArea, name='agregarArea'),
    path('menuAdmin/listaAreas/deleteArea/<int:id_>', views.deleteArea, name='deleteArea'),
    path('menuAdmin/listaAreas/updateArea/<int:id_>', views.updateArea, name='updateArea'),
    path('menuAdmin/listaAreas/areasInfoAdmin/<int:id_>', views.readArea, name='areasInfoAdmin'),
    path('menuAdmin/listaAreas/areasInfoAdmin/agregarElemento/<int:idArea>/', views.createElemento, name='agregarElemento'),
    path('menuAdmin/listaAreas/areasInfoAdmin/<int:id_>/deleteElemento/<int:idArea>/<int:idElemento>/', views.deleteElemento, name='deleteElemento'),
    path('menuAdmin/listaAreas/areasInfoAdmin/readElemento/<int:idArea>/<int:idElemento>/', views.readElemento, name='readElemento'),
    path('menuAdmin/listaAreas/areasInfoAdmin/<int:id_>/updateElemento/<int:idArea>/<int:idElemento>/', views.updateElemento, name='updateElemento'),
    path('menuAdmin/verAgentesDeterioro/', views.verAgentesDeterioro, name='verAgentesDeterioro'),
    path('menuAdmin/asignacionTrabajoLista/', views.asignacionTrabajoLista, name='asignacionTrabajoLista'),
    path('menuAdmin/asignacionTrabajoLista/preAsignacionTrabajo/<int:id_>/', views.preAsignacionTrabajo, name='preAsignacionTrabajo'),
    path('menuAdmin/asignacionTrabajoLista/preAsignacionTrabajo/<int:id_>/asignacion/<int:idA>', views.createInspeccion, name='asignacion'),
    path('menuAdmin/listInspeccion/', views.listInspeccion, name='listInspeccion'),
    path('menuAdmin/listaUsuarios/', views.listUsers, name='listaUsuarios'),
    #Links de super usuario
    path('menuSuper/', views.menuAdmin, name='menuSuperUsuario'),
    #Links de trabajadores

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
