from django.urls import path
from apppaginacoder.views import inicio, profesor, estudiante, entregable, cursos, agregar_curso, lista_curso

urlpatterns = [
    path('lista-curso', lista_curso),
    path('agregar-curso/<nombre>/<camada>', agregar_curso),
    path('' , inicio , name='Inicio'),
    path('profesor/' , profesor , name='Profesores'),
    path('estudiante/' , estudiante , name='Estudiantes'),
    path('entregable/' , entregable , name='Entregable'),
    path('cursos/' , cursos , name='Cursos'),
]
