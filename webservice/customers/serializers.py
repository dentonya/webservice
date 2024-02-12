from .models import Customers
from rest_framework import serializers

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields ='__all__'