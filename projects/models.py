from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Users(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    rol = models.IntegerField(default=1)
    password = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)

    

