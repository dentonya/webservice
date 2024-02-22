from rest_framework import viewsets,permissions
from .models import Customers
from .serializers import CustomersSerializer
from rest_framework.permissions import AllowAny

class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [AllowAny]
    queryset =Customers.objects.all()
    serializer_class = CustomersSerializer