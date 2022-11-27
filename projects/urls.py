from rest_framework import routers
from .api import UsersViewSet, DistritosViewSet , ParaderosViewSet ,JornadasViewSet,RutasViewSet, UsuariosViewSet,EmpresasViewSet , UnidadesViewSet

router = routers.DefaultRouter()

router.register('api/Users' ,UsersViewSet)
#router.register('op-filter', views.op_listView, basename='op-filter')

#==================== WEB PAGINE ==============#
router.register('api/distritos' ,DistritosViewSet , 'distritos' )
router.register('api/paraderos' ,ParaderosViewSet , 'paraderos' )
router.register('api/jornadas' ,JornadasViewSet , 'jornadas' )
router.register('api/rutas' ,RutasViewSet , 'rutas' )
router.register('api/usuarios' ,UsuariosViewSet , 'usuarios' )
router.register('api/empresas' ,EmpresasViewSet , 'empresas' )
router.register('api/unidades' ,UnidadesViewSet , 'unidades')
#router.register('api/rutas2' ,Rutas2ViewSet , 'rutas2' )

urlpatterns = router.urls