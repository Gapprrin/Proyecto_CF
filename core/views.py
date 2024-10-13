from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

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