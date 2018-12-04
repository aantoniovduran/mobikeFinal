from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):
    Primer_nombre = models.CharField(max_length=50)
    Segundo_nombre = models.CharField(max_length=50)
    Apellido_paterno = models.CharField(max_length=50)
    Apellido_materno = models.CharField(max_length=50)
    Rut = models.CharField(max_length=10)
    Telefono = models.IntegerField()
    Email = models.EmailField()
    Direccion = models.TextField()
    Comuna_trabajo = models.CharField(max_length=50)
    Nombreusuario = models.CharField(max_length=50)
    Contraseña = models.CharField(max_length=50)
    Banco = models.CharField(max_length=50)
    numerotarjeta = models.IntegerField()
    
    def __str__(self):
        return self.Rut
