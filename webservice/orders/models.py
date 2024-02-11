from django.db import models
from customers.models import Customers

# Create your models here.
class Orders(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    amount = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)