from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def createUser(request):
    return render(request, "create_user.html")

def solicitudForm(request):
    return render(request, "form.html")