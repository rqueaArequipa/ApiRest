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
from .models import Users, Distritos , Paraderos ,Jornadas ,Rutas , Usuarios ,Empresas ,Unidades

def UsersJson(request):
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
   return JsonResponse(data, safe=False)


def Home(request):
   return HttpResponse('<a href="http://127.0.0.1:8000/api/distritos/">LInk</a><a href="https://www.tiktok.com/es">LInk</a>')

