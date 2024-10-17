from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms

class Registro(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

class RegistroSolicitud(forms.ModelForm):

    class Meta:
        model = SolicitudRetiro
        fields = ("tipo_residuo", "cant_residuos", "direccion", "descripcion", "usuario")
