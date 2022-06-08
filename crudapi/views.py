from django.shortcuts import render
from rest_framework import viewsets

from crudapi.models import Product
from crudapi.serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
