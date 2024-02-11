from .models import Customers
from rest_framework import serializers

class CustomerfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields ='__all__'