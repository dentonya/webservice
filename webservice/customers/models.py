from django.db import models

# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15,null=False)