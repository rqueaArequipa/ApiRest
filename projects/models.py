from django.db import models

# Create your models here


class Users(models.Model):
    name = models.CharField(max_length=30, null=True)
    lastname = models.CharField(max_length=30 )
    email = models.EmailField(unique=True)
    rol = models.IntegerField(default=1)
    password = models.CharField(max_length=20 )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


#clases de PAGINA WEB
class Distritos(models.Model):
    nombre = models.CharField(max_length=100 , unique=True)
    imagen = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.nombre
    
    
    
class Paraderos(models.Model):
    ubicacion = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    imagen = models.CharField(max_length=250, null=True)  
    
    def __str__(self):
        return self.ubicacion  
    
    
class Jornadas(models.Model):
    inicio = models.CharField(max_length=200)
    final= models.CharField(max_length=200)
   
    
    def __str__(self):
        return self.inicio     
    
    
   
   
    

class Rutas(models.Model):
    nombre = models.CharField(max_length=200)
    inicio = models.CharField(max_length=200)
    final = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    paraderos_id = models.ForeignKey(Paraderos, null=True, blank=True, on_delete=models.CASCADE)
    distrito_id = models.ForeignKey(Distritos, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password= models.CharField(max_length=200)
    distrito_id = models.ForeignKey(Distritos ,null=True, blank=True, on_delete=models.CASCADE)
    
    def __st__(self):
        return self.nombre    

class Empresas(models.Model):
    nombre = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    distrito_id = models.ForeignKey(Distritos ,null=True, blank=True, on_delete=models.CASCADE)
    imagen = models.CharField(max_length=250, null=True) 
    rutas_id = models.ForeignKey(Rutas , null=True, blank=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre  
    
    
class Unidades(models.Model):
    conductor = models.CharField(max_length=200)
    placa= models.CharField(max_length=200)
    longitud= models.CharField(max_length=200)
    capacidad = models.IntegerField()
    lapso_tiempo=models.CharField(max_length=200)
    empresas_id = models.ForeignKey(Empresas ,null=True, blank=True, on_delete=models.CASCADE)
    distrito_id = models.ForeignKey(Distritos ,null=True, blank=True, on_delete=models.CASCADE)
    rutas_id = models.ForeignKey(Rutas ,null=True, blank=True, on_delete=models.CASCADE)
    jornadas_id = models.ForeignKey(Jornadas ,null=True, blank=True, on_delete=models.CASCADE)
    
   
    def __str__(self):
        return self.placa


class Comentarios(models.Model):
    comentario = models.TextField()
    usuario_id = models.ForeignKey(Usuarios ,null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comentario

''''class Rutas2(models.Model):
    nombre = models.CharField(max_length=200)
    inicio = models.CharField(max_length=200)
    final = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    paraderos_id = models.ForeignKey(Paraderos, on_delete=models.CASCADE)
    distritos_id = models.ForeignKey(Distritos, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre'''


    

