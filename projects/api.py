from .models import Rutas2, Users, Distritos , Paraderos ,Jornadas ,Rutas , Usuarios ,Empresas ,Unidades
from rest_framework import viewsets, permissions, filters
from .serializers import  Rutas2Serializer, UsersSerializer, DistritosSerializer , ParaderosSerializer , JornadasSerializer , RutasSerializer , UnidadesSerializer,EmpresasSerializer,UsuariosSerializer
from rest_framework.permissions import IsAuthenticated
#import django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsersSerializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id' , 'name' , 'lastname' , 'email' , 'rol', 'password']
    search_fields = ['id' , 'name' , 'lastname' , 'email' , 'rol', 'password']
    #filter_backends = []
    #filter_backends =[filters.OrderingFilter]
    #filter_fields = ["id" , "name" , "lastname" , "email" , "rol", "password"]
    #filter_fields = ["id" , "name" , "lastname" , "email" , "rol", "password"]
    

#=================WEB PAGINE =================================#
class DistritosViewSet(viewsets.ModelViewSet):
    
    
    queryset = Distritos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DistritosSerializer
    
    #Filtros
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'nombre']
    search_fields = ['id', 'nombre']
    
    
    
class ParaderosViewSet(viewsets.ModelViewSet):
    queryset = Paraderos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ParaderosSerializer   

    #Filtros
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id' , 'ubicacion' , 'descripcion']
    search_fields = ['id' , 'ubicacion' , 'descripcion']
    
    
class JornadasViewSet(viewsets.ModelViewSet):
    queryset = Jornadas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = JornadasSerializer

    #Filtros
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id' , 'inicio' , 'final']
    search_fields = ['id' , 'inicio' , 'final']
    
    
class RutasViewSet(viewsets.ModelViewSet):
    queryset = Rutas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RutasSerializer

    #Filtros
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id' , 'nombre' , 'inicio' , 'final' , 'descripcion', 'paraderos_id']
    search_fields = ['id' , 'nombre' , 'inicio' , 'final' , 'descripcion', 'paraderos_id']
    
    
class UsuariosViewSet(viewsets.ModelViewSet):
    
    queryset = Usuarios.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuariosSerializer

    #Filtros
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id' , 'nombre' , 'email' , 'password' , 'distritos_id']
    search_fields = ['id' , 'nombre' , 'email' , 'password' , 'distritos_id']
    
    
class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmpresasSerializer

    #Filtros
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id' , 'nombre' , 'cantidad' , 'distrito_id' , 'rutas_id']
    search_fields = ['id' , 'nombre' , 'cantidad' , 'distrito_id' , 'rutas_id']
    
    
class UnidadesViewSet(viewsets.ModelViewSet):
    queryset = Unidades.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UnidadesSerializer

    #Filtros
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id' , 'conductor' , 'placa' , 'longitud' , 'capacidad', 'lapso_tiempo', 'empresas_id' , 'distrito_id' , 'rutas_id' , 'jornadas_id']
    search_fields = ['id' , 'conductor' , 'placa' , 'longitud' , 'capacidad', 'lapso_tiempo', 'empresas_id' , 'distrito_id' , 'rutas_id' , 'jornadas_id']

class Rutas2ViewSet(viewsets.ModelViewSet):
    queryset = Rutas2.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Rutas2Serializer  
     #Filtros
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id' , 'nombre' , 'inicio' , 'final' , 'descripcion', 'paraderos_id', 'distritos_id']
    search_fields = ['id' , 'nombre' , 'inicio' , 'final' , 'descripcion', 'paraderos_id', 'distritos_id']

    
