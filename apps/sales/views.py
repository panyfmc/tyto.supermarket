from django.shortcuts import render
from .models import Sale
from .serializers import SaleSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

class SaleViewSet(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]

def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sales.html', {'sales': sales})
