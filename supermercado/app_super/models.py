from mailbox import NoSuchMailboxError
from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre}"


class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField()
    nacimiento = models.DateField()
    documento = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}"


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}"


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre}"