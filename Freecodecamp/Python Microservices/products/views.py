from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

class ProductViewSet(viewsets.Viewset):
    def list(self, request):  #/api/products
        products = Product.objects.all()

    def create(self, request):  #/api/products
        pass

    def retrieve(self, request, pk=None):  #/api/products/<str:id>
        pass

    def update(self, request, pk=None):  #/api/products/<str:id>
        pass

    def destroy(self, request, pk=None):   #/api/products/<str:id>
        pass