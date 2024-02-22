import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webservice.settings')
django.setup()

from rest_framework import status
from django.test import TestCase
from customers.models import Customers
from orders.models import Orders
from rest_framework.test import APIClient

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customers.objects.create(name='Test Customer', code='TC001',phone_number='0123456789')
        self.order = Orders.objects.create(customer=self.customer, item='Test Item', amount=1)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer YOUR_ACCESS_TOKEN')

    def tearDown(self):
        Customers.objects.all().delete()
        
         # Include OAuth2 authentication headers

    def test_customer_create_view(self):
        response = self.client.post('/api/customer/', {'name': 'New Customer', 'code': 'NC001','phone_number':'0123456789'})
        print(response.content) 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customers.objects.count(),  3)
        self.assertEqual(Customers.objects.get(code='NC001').name, 'New Customer')

    def test_order_create_view(self):
        response = self.client.post('/api/order/', {'customer': self.customer.id, 'item': 'New Item', 'amount':  2})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Orders.objects.count(),  2)
        self.assertEqual(Orders.objects.get(item='New Item').amount,  2)
   