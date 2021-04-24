from rest_framework import serializers
from articulo import models


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'nombre',
            'descripcion',
            'stock',
            'precio',
            'marca',
            'modelo',
            'dimensiones',
            'disponible'
        )
        model = models.Articulo


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'nombre',
            'descripcion',
            'activa'
        )
        model = models.Categoria
