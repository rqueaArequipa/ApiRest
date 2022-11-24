from .models import Project, Users
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer, UsersSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsersSerializer