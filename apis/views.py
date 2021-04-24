from django.shortcuts import render
from rest_framework import generics

from articulo import models
from .serializers import ArticuloSerializer, CategoriaSerializer


# Create your views here.
class ListArticulo(generics.ListCreateAPIView):
    queryset = models.Articulo.objects.all()
    serializer_class = ArticuloSerializer


class DetailArticulo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Articulo.objects.all()
    serializer_class = ArticuloSerializer


class ListCategoria(generics.ListCreateAPIView):
    queryset = models.Categoria.objects.all()
    serializer_class = CategoriaSerializer


class DetailCategoria(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Categoria.objects.all()
    serializer_class = CategoriaSerializer
