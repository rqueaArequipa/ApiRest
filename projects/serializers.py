from rest_framework import serializers
from .models import Project, Users, Distritos , Paraderos ,Jornadas ,Rutas , Usuarios ,Empresas ,Unidades

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at', )

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ("id" , "name" , "lastname" , "email" , "rol", "password", "created_at")
        

#PAGINA WEB ++++++++++====================================

class DistritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distritos
        fields = ("id" , "nombre", 'imagen' )
        
class ParaderosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paraderos
        fields = ("id" , "ubicacion" ,"descripcion" , "imagen" )     
        
class JornadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jornadas
        fields = ("id" , "inicio" , "final")  
        
class RutasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutas
        fields = ("id" , "nombre" ,"inicio" , "final" , "descripcion" , "paraderos_id" )      
        
        
class UsuariosSerializer(serializers.ModelSerializer):
    #distritos_id =serializers.CharField(source = 'distritos_id.nombre')
    class Meta:
        model = Usuarios
        fields = ("id" , "nombre" , "email" , "password" , "distritos_id")                   
        
class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = ("id" , "nombre" , "cantidad" , "distrito_id" , "imagen" ,"rutas_id")        
        
        
class UnidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidades
        fields = ("id" , "conductor" , "placa" , "longitud" , "capacidad" ,"lapso_tiempo" , "empresas_id" ,
                  "distrito_id" , "rutas_id" , "jornadas_id")


    