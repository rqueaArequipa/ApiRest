"""projectend URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from projects.api import DistritosWeb, ParaderosWeb, RutasWeb, EmpresasWeb
from rest_framework.authtoken import views
from projects.views import Home, Apis, Service

#extras
from django.http import HttpRequest


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('__debug__', include(debug_toolbar.urls))

    #path('api_authorization/', include('rest_framework.urls')),
   # path('person/',PeronaList.as_view(), name = 'persona_list'),
    #path('home/',UsersViewSet.as_view(), name = 'List_user'),

    #A vista de Todos
    path('Distritos/',DistritosWeb.as_view(), name = 'distritos'),
    path('Paraderos/',ParaderosWeb.as_view(), name = 'distritos'),
    path('Rutas/',RutasWeb.as_view(), name = 'distritos'),
    path('Empresas/',EmpresasWeb.as_view(), name = 'distritos'),

    #ruta apis
    path ('717ab3b1503b549a393b14f0740a1312c90c29da/', include('projects.urls')),

    #path('api_genere_token/', views.obtain_auth_token),
    #path('Login/', Login.as_view(), name='login'),
    path('', Home.as_view(), name='Home'),
    path('Apis/', Apis.as_view(), name='apis'),
    path('Service/', Service.as_view(), name='Services'),

    #router.register('api/paraderos' ,ParaderosViewSet , 'paraderos' )
#router.register('api/jornadas' ,JornadasViewSet , 'jornadas' )
#router.register('api/rutas' ,RutasViewSet , 'rutas' )
#router.register('api/usuarios' ,UsuariosViewSet , 'usuarios' )
#router.register('api/empresas' ,EmpresasViewSet , 'empresas' )
#router.register('api/unidades' ,UnidadesViewSet , 'unidades')
#router.register('api/rutas2' ,Rutas2ViewSet , 'rutas2' )
    


    #Url Template
    #path('', Contact)

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
