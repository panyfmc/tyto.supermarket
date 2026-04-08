from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M")

    class Meta:
        model = Client
        fields = '__all__'