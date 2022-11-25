from .models import Project, Users, Distritos , Paraderos ,Jornadas ,Rutas , Usuarios ,Empresas ,Unidades
from rest_framework import viewsets, permissions, filters
from .serializers import ProjectSerializer, UsersSerializer, DistritosSerializer , ParaderosSerializer , JornadasSerializer , RutasSerializer , UnidadesSerializer,EmpresasSerializer,UsuariosSerializer
from rest_framework.permissions import IsAuthenticated
#import django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsersSerializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['id' , 'name' , 'lastname' , 'email' , 'rol', 'password']
    #search_fields = ['nombre']
    #filter_backends = []
    #filter_backends =[filters.OrderingFilter]
    #filter_fields = ["id" , "name" , "lastname" , "email" , "rol", "password"]
    #filter_fields = ["id" , "name" , "lastname" , "email" , "rol", "password"]
    

#=================WEB PAGINE =================================#
class DistritosViewSet(viewsets.ModelViewSet):
    
    
    queryset = Distritos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DistritosSerializer
    
    filter_backends =[filters.SearchFilter]
    search_fields = ['nombre']
    
    
    
class ParaderosViewSet(viewsets.ModelViewSet):
    queryset = Paraderos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ParaderosSerializer   
    
    
class JornadasViewSet(viewsets.ModelViewSet):
    queryset = Jornadas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = JornadasSerializer
    
    
class RutasViewSet(viewsets.ModelViewSet):
    queryset = Rutas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RutasSerializer
    
    
class UsuariosViewSet(viewsets.ModelViewSet):
    
    
    
    queryset = Usuarios.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuariosSerializer
    
    
class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmpresasSerializer
    
    
class UnidadesViewSet(viewsets.ModelViewSet):
    queryset = Unidades.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UnidadesSerializer


    
