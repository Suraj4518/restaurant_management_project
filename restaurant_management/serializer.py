
from rest_framework import serializers

class MenuItemSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
