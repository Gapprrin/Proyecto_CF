from django.db import models
from django.contrib.auth.forms import User

# Super user: umbre, 12345678op

# Create your models here.

class TipoResiduo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_residuo = models.CharField(max_length=25)

    def __str__ (self):
        return self.nombre_residuo


class SolicitudRetiro(models.Model):
    id = models.AutoField(primary_key=True)
    cant_residuos = models.IntegerField()
    tipo_residuo = models.ForeignKey(to=TipoResiduo, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=400, null=True)
    destino_final = models.CharField(max_length=100, null=True)
    ruta_optima = models.CharField(max_length=300, null=True)
    valor = models.IntegerField(null=True)
    usuario = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_residuo.nombre_residuo + " " + self.usuario.username

