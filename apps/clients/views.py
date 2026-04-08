from django.shortcuts import render
from .models import Client
from .serializers import ClientSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})
