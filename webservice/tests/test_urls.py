import os
import django
from rest_framework import status

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webservice.settings')
django.setup()
from django.test import TestCase
from rest_framework.test import APIClient
from customers.models import Customers
from orders.models import Orders

class UrlsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customers.objects.create(name='Test Customer', code='TC001')
        self.order = Orders.objects.create(customer=self.customer, item='Test Item', amount=1)

        # Include OAuth2 authentication headers
        self.client.credentials(HTTP_AUTHORIZATION='Bearer YOUR_ACCESS_TOKEN')

    def test_customer_list_url(self):
        response = self.client.get('/api/customer/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.customer.name)

    def test_order_list_url(self):
        response = self.client.get('/api/order/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.order.item)
