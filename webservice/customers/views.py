from rest_framework import viewsets
from .models import Customers
from .serializers import CustomersSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset =Customers.objects.all()
    serializer_class = CustomersSerializer