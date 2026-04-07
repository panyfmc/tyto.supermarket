from rest_framework import serializers
from .models import Sale

class SaleSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%d/%m/%Y %H:%M")
    class Meta:
        model = Sale
        fields = '__all__'