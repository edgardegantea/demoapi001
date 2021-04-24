from django.urls import path

from .views import ListArticulo, DetailArticulo, DetailCategoria, ListCategoria

urlpatterns = [
    path('articulo', ListArticulo.as_view()),
    path('articulo/<int:pk>/', DetailArticulo.as_view()),
    path('categoria', ListCategoria.as_view()),
    path('categoria/<int:pk>/', DetailCategoria.as_view()),
]