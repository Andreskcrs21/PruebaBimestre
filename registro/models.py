from django.db import models
from datetime import datetime

# Create your models here.

class UsuarioEquipos(models.Model):
    Usuario = models.CharField(max_length=100)
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    Correo = models.CharField(max_length=100)
    Equipo_Nombre = models.CharField(max_length=100)
    Diagnostico = models.CharField(max_length=500)
    FechaIngreso = models.DateTimeField("Fecha de Ingreso", default=datetime.now())

