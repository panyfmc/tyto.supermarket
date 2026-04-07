from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})
