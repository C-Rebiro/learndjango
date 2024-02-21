from django.shortcuts import render
from django.http import HttpResponse


def karibu(request):
    return HttpResponse("<h1>Karibu django</h1>")

def homepage(request):
    return render(request, "index.html")

def about(request):
    return render(request, "About us.html")

def contact(request):
    return render(request, "contcat us.html")

def gallery(request):
    return render(request, "gallery.html")

def services(request):
    return render(request, "services.html")

