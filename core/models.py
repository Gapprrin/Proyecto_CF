from django.db import models
from django.contrib.auth.forms import User

# Super user: umbre, 12345678op

# Create your models here.

class SolicitudRetiro(models.Model):
    id = models.AutoField(primary_key=True)
    cant_residuos = models.IntegerField(),
    tipo_residuo = models.CharField(max_length=14),
    usuario = models.ForeignKey(to=User, on_delete=models.CASCADE),
    direccion = models.CharField(max_length=100),
    descripcion = models.CharField(max_length=400)

    def __str__(self):
        return self.tipo_residuo

