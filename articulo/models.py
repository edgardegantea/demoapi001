from django.db import models


# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=100, unique=True)
    descripcion = models.CharField(verbose_name='Descripción', max_length=200, null=True)
    stock = models.PositiveIntegerField(verbose_name='Stock', default=0)
    precio = models.DecimalField(verbose_name='Precio', default=0.00, max_digits=6, decimal_places=2)
    marca = models.CharField(verbose_name='Marca', max_length=50)
    modelo = models.CharField(verbose_name='Modelo', max_length=50)
    dimensiones = models.CharField(verbose_name='Dimensiones', max_length=100)
    OPCIONES = [('sí', 'sí'), ('no', 'no')]
    disponible = models.CharField(verbose_name='Disponible', max_length=2, choices=OPCIONES, default='sí')

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(verbose_name="Categoría", max_length=150, unique=True)
    descripcion = models.TextField(verbose_name="Descripción de la categoría")
    activa = models.BooleanField(verbose_name="Activa", default=True)Actraa

    def __str__(self):
        return self.nombre

