from .models import Project, Users
from rest_framework import viewsets, permissions, filters
from .serializers import ProjectSerializer, UsersSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsersSerializer
    filter_backends =[filters.SearchFilter]
    search_fields = ["id" , "name" , "lastname" , "email" , "rol", "password"]
    
