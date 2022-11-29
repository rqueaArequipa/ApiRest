from django.shortcuts import render

# Create your views here.
#from django_filters.rest_framework import DjangoFilterBackend
#from .models import Users
#from .serializers import UsersSerializer
#from rest_framework import generics



#class UserFilter(generics.ListAPIView):
   # queryset = Users.objects.all()
    #serializer_class = UsersSerializer
    #filter_backends = [DjangoFilterBackend]

    #filterset_fields = ['id' , 'name' , 'lastname' , 'email' , 'rol', 'password']

from django.http import JsonResponse, HttpResponse
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
#import django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from .models import (Distritos, Empresas, Jornadas, Paraderos, Rutas,
                     Unidades, Users, Usuarios, Comentarios)
from .serializers import (DistritosSerializer, EmpresasSerializer,
                          JornadasSerializer, ParaderosSerializer, RutasSerializer,
                          UnidadesSerializer, UsersSerializer,
                          UsuarioSerializer, UsuariosSerializer, ComentarioSerializer)

####################===========APIS================================####################
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classess = [permissions.AllowAny]
    serializer_class = UsersSerializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id' , 'name' , 'lastname' , 'email' , 'rol', 'password']
    search_fields = ['id' , 'name' , 'lastname' , 'email' , 'rol', 'password']
    

#=================WEB PAGINE =================================#
class DistritosViewSet(viewsets.ModelViewSet):
    queryset = Distritos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DistritosSerializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'nombre']
    search_fields = ['id', 'nombre']
    
    
    
class ParaderosViewSet(viewsets.ModelViewSet):
    queryset = Paraderos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ParaderosSerializer   
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id' , 'ubicacion' , 'descripcion']
    search_fields = ['id' , 'ubicacion' , 'descripcion']
    
    
class JornadasViewSet(viewsets.ModelViewSet):
    queryset = Jornadas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = JornadasSerializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id' , 'inicio' , 'final']
    search_fields = ['id' , 'inicio' , 'final']
    
    
class RutasViewSet(viewsets.ModelViewSet):
    queryset = Rutas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RutasSerializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id' , 'nombre' , 'inicio' , 'final' , 'descripcion', 'paraderos_id', 'distrito_id']
    search_fields = ['id' , 'nombre' , 'inicio' , 'final' , 'descripcion', 'paraderos_id', 'distrito_id']
    
    
class UsuariosViewSet(viewsets.ModelViewSet):
    
    queryset = Usuarios.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuariosSerializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id' , 'nombre' , 'email' , 'password' , 'distrito_id']
    search_fields = ['id' , 'nombre' , 'email' , 'password' , 'distrito_id']
    
    
class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmpresasSerializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id' , 'nombre' , 'cantidad' , 'distrito_id' , 'rutas_id']
    search_fields = ['id' , 'nombre' , 'cantidad' , 'distrito_id' , 'rutas_id']
    
    
class UnidadesViewSet(viewsets.ModelViewSet):
    queryset = Unidades.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UnidadesSerializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id' , 'conductor' , 'placa' , 'longitud' , 'capacidad', 'lapso_tiempo', 'empresas_id' , 'distrito_id' , 'rutas_id' , 'jornadas_id']
    search_fields = ['id' , 'conductor' , 'placa' , 'longitud' , 'capacidad', 'lapso_tiempo', 'empresas_id' , 'distrito_id' , 'rutas_id' , 'jornadas_id']

class ComentariosViewSet(viewsets.ModelViewSet):
   queryset = Comentarios.objects.all()
   permission_classes = [permissions.AllowAny]
   serializer_class = ComentarioSerializer
   filter_backends =[DjangoFilterBackend, filters.SearchFilter]
   filterset_fields = ['id' , 'comentario' , 'usuario_id']
   search_fields = ['id' , 'comentario' , 'usuario_id']

'''def UsersJson(request):
   data =list(Users.objects.values())
   return JsonResponse(data, safe=False)

def DistritosJson(request):
   data =list(Distritos.objects.values())
   return JsonResponse(data, safe=False)

def ParaderosJson(request):
   data =list(Paraderos.objects.values())
   return JsonResponse(data, safe=False)

def JornadasJson(request):
   data =list(Jornadas.objects.values())
   return JsonResponse(data, safe=False)

def RutasJson(request):
   data =list(Rutas.objects.values())
   return JsonResponse(data, safe=False)

def UsuariosJson(request):
   data =list(Usuarios.objects.values())
   return JsonResponse(data, safe=False)

def EmpresasJson(request):
   data =list(Empresas.objects.values())
   return JsonResponse(data, safe=False)

def UnidadesJson(request):
   data =list(Unidades.objects.values())
   return JsonResponse(data, safe=False)'''

class Home(FormView):
   template_name = "index.html"
   form_class = AuthenticationForm

class Apis(FormView):
   template_name = "apis.html"
   form_class = AuthenticationForm

class Service(FormView):
   template_name = "servicios.html"
   form_class = AuthenticationForm


