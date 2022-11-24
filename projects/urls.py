from rest_framework import routers
from .api import ProjectViewSet, UsersViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet)
router.register('api/Users' ,UsersViewSet)

urlpatterns = router.urls