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
                     Unidades, Users, Usuarios)
from .serializers import (DistritosSerializer, EmpresasSerializer,
                          JornadasSerializer, ParaderosSerializer, RutasSerializer,
                          UnidadesSerializer, UsersSerializer,
                          UsuarioSerializer, UsuariosSerializer)


'''class PeronaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    authentication_classes = [TokenAuthentication]'''
    

class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    permission_classess = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    #success_url = reverse_lazy('home')
    success_url = reverse_lazy('List_user')


    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,*kwargs)

    def form_valid(self,form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = user)
        if token:
            login(self.request, form.get_user())
            return super(Login,self).form_valid(form)

#=================WEB PAGINE =================================#
class DistritosWeb(generics.ListCreateAPIView):
    queryset = Distritos.objects.all()
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = DistritosSerializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'nombre']
    search_fields = ['id', 'nombre']
     
class ParaderosWeb(generics.ListCreateAPIView):
    queryset = Paraderos.objects.all()
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = ParaderosSerializer   
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id' , 'ubicacion' , 'descripcion']
    search_fields = ['id' , 'ubicacion' , 'descripcion']
    
class RutasWeb(generics.ListCreateAPIView):
    queryset = Rutas.objects.all()
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = RutasSerializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id' , 'nombre' , 'inicio' , 'final' , 'descripcion', 'paraderos_id', 'distrito_id']
    search_fields = ['id' , 'nombre' , 'inicio' , 'final' , 'descripcion', 'paraderos_id', 'distrito_id']
    
class EmpresasWeb(generics.ListCreateAPIView):
    queryset = Empresas.objects.all()
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = EmpresasSerializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id' , 'nombre' , 'cantidad' , 'distrito_id' , 'rutas_id']
    search_fields = ['id' , 'nombre' , 'cantidad' , 'distrito_id' , 'rutas_id']
    

'''class Rutas2ViewSet(viewsets.ModelViewSet):
    queryset = Rutas2.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Rutas2Serializer  
     #Filtros
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id' , 'nombre' , 'inicio' , 'final' , 'descripcion', 'paraderos_id', 'distritos_id']
    search_fields = ['id' , 'nombre' , 'inicio' , 'final' , 'descripcion', 'paraderos_id', 'distritos_id']'''

    
