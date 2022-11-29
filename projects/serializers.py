from rest_framework import serializers
from .models import Users, Distritos , Paraderos ,Jornadas ,Rutas , Usuarios ,Empresas ,Unidades, Comentarios

from django.contrib.auth.models import User

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        moel = User
        fields = ('id', 'username', 'password','is_staff')
        extra_kwargs = {'password': {'write_only':True}}

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ("id" , "name" , "lastname" , "email" , "rol", "password")
        

#PAGINA WEB ++++++++++====================================

class DistritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distritos
        fields = ("__all__")
        
class ParaderosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paraderos
        fields = ("__all__")     
        
class JornadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jornadas
        fields = ("__all__")  
        
class RutasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutas
        fields = ("__all__")      
        
        
class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ("__all__")                   
        
class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = ("__all__")        
        
        
class UnidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidades
        fields = fields = ("__all__")

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = fields = ("__all__")


'''class Rutas2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Rutas2
        fields = ("id" , "nombre" ,"inicio" , "final" , "descripcion" , "paraderos_id" , "distritos_id") '''


    