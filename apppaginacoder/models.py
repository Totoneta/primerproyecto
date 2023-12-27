from django.db import models

# Create your models here.
class profesor(models.Model):
    nombre = models.CharField(("Nombre"), max_length=50)
    apellido = models.CharField(("Apellido"), max_length=50)
    fecha_comienzo = models.DateField("Fecha de ingreso")
    dni = models.IntegerField("Dni(Sín puntos)")
    profe_de = models.CharField("Profesor de", max_length=50)
    email = models.EmailField(("Email"), max_length=254)

class estudiante(models.Model):
    nombre = models.CharField(("Nombre"), max_length=50)
    apellido = models.CharField(("Apellido"), max_length=50)
    dni = models.IntegerField("Dni(Sín puntos)")
    cursando = models.CharField("Cursando", max_length=50)
    email = models.EmailField(("Email"), max_length=130)

class curso(models.Model):
    nombre = models.CharField("Nombre de curso", max_length=60)
    camada = models.IntegerField("Camada")

class entregable(models.Model):
    nombre = models.CharField("Nombre", max_length=150)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()