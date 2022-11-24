from rest_framework import serializers
from .models import Project, Users

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at', )

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ("id" , "name" , "lastname" , "email" , "rol", "password", "created_at")
    