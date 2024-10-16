from django.shortcuts import render
from django.contrib.auth.views import logout_then_login

# Create your views here.

def home(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def logout(request):
    return logout_then_login(request, 'login')

def createUser(request):
    return render(request, "create_user.html")

def retiroResiduos(request):
    return render(request, "retiro_residuos.html")

def registrarse(request):
    return render(request, 'registrarse.html')

def pagAdmin(request):
    return render(request, 'pagAdmin.html')

def historial(request):
    return render(request, 'historial.html')