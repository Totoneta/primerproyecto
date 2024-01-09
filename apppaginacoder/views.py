from django.shortcuts import render
from django.http import HttpResponse
from .models import curso

def lista_curso (request):
    lista = curso.objects.all()
    return render(request, 'lista_cursos.html', {"lista_curso" : lista})

def agregar_curso(request, nombre, camada):
    nuevo = curso(nombre=nombre, camada=camada)
    nuevo.save()
    return HttpResponse(f'El curso:{curso.nombre}, camada:{curso.camada}')

def inicio(request):
    return render(request, 'index.html')

def profesor(request):
    return render(request, "profesor.html")

def entregable(request):
    return render(request, "entregable.html")

def estudiante(request):
    return render(request, "estudiante.html")

def cursos(request):
    return render(request, "cursos.html")