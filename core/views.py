from django.shortcuts import render, redirect
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.forms import UserCreationForm
from .forms import *

# Create your views here.

def home(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def logout(request):
    return logout_then_login(request, 'login')

def retiroResiduos(request):
    if request.method == "POST":
        registro = RegistroSolicitud(request.POST)
        if registro.is_valid():
            registro.save()
            return render(request, "retiro_residuos.html", {"form" : registro})
    else:
        registro = RegistroSolicitud()
        
    return render(request, "retiro_residuos.html", {"form" : registro})


def registrarse(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to='login')
    else:
        registro = Registro()
    return render(request, "registrarse.html", {"form" : registro})

def pagAdmin(request):
    return render(request, 'pagAdmin.html')

def historial(request):
    registros = SolicitudRetiro.objects.filter(usuario = request.user.id)
    return render(request, 'historial.html', {"registros" : registros})