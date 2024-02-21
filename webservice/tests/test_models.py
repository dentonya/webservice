import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webservice.settings')
django.setup()

from django.test import TestCase
from customers.models import Customers
from orders.models import Orders

class CustomerTestCase(TestCase):
    def test_customer_creation(self):
        customer = Customers.objects.create(name='Test Customer', code='TC001')
        self.assertEqual(customer.name, 'Test Customer')
        self.assertEqual(customer.code, 'TC001')

class OrderTestCase(TestCase):
    def test_order_creation(self):
        customer = Customers.objects.create(name='Test Customer', code='TC001')
        order = Orders.objects.create(customer=customer, item='Test Item', amount=1)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.item, 'Test Item')
        self.assertEqual(order.amount,  1)
