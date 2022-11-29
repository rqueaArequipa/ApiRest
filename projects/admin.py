from django.contrib import admin

# Register your models here.

from .models import Users, Distritos , Paraderos ,Jornadas ,Rutas , Usuarios ,Empresas ,Unidades, Comentarios

#admin.site.register(Users)
'''admin.site.register(Distritos)
admin.site.register(Paraderos)
admin.site.register(Jornadas)
admin.site.register(Rutas)
admin.site.register(Usuarios)
admin.site.register(Empresas)
admin.site.register(Unidades)'''
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("id" , "name" , "lastname" , "email" , "rol", "password", "created_at")

    list_per_page = 10

@admin.register(Distritos)
class DistritosAdmin(admin.ModelAdmin):
    list_display = ("id" , "nombre", 'imagen' )
    list_per_page = 10

@admin.register(Paraderos)
class ParaderoAdmin(admin.ModelAdmin):
    list_display = ("id" , "ubicacion" ,"descripcion" , "imagen" )
    list_per_page = 10

@admin.register(Jornadas)
class JornadaAdmin(admin.ModelAdmin):
    list_display = ("id" , "inicio" , "final")
    list_per_page = 10

@admin.register(Rutas)
class RutaAdmin(admin.ModelAdmin):
    list_display = ("id" , "nombre" ,"inicio" , "final" , "descripcion" , "paraderos_id", 'distrito_id' )
    list_per_page = 10

@admin.register(Usuarios)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id" , "nombre" , "email" , "password" , "distrito_id")
    list_per_page = 10

@admin.register(Empresas)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("id" , "nombre" , "cantidad" , "distrito_id" , "imagen" ,"rutas_id")
    list_per_page = 10

@admin.register(Unidades)
class UnidadesAdmin(admin.ModelAdmin):
    list_display = ("id" , "conductor" , "placa" , "longitud" , "capacidad" ,"lapso_tiempo" , "empresas_id" ,
                  "distrito_id" , "rutas_id" , "jornadas_id")
    list_per_page = 10

@admin.register(Comentarios)
class ComentariosAdmin (admin.ModelAdmin):
    list_display = ("id","comentario","usuario_id")

    list_per_page = 10
