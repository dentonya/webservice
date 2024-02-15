from rest_framework import viewsets
from rest_framework.response import Response
from .models import Orders
from .serializers import OrderSerializer
import africastalking

# Initialize the Africa's Talking SDK
africastalking.initialize(username='username', api_key='api-key')

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        # Save the order
        instance = serializer.save()

        # Get the customer's phone number from the related customer model
        customer_phone_number = instance.customer.phone_number  # Adjust field name as necessary
        # Prepare the SMS message
        order_message = f"Thank you for your order! Your order for {instance.item} has been successfully placed."

        # Access the SMS service
        sms = africastalking.SMS

        # Send SMS
        response = sms.send(message=order_message, recipients=[customer_phone_number])

        # Check the response and handle errors if needed
        if response['SMSMessageData']['Recipients'][0]['status'] == 'Success':
            # SMS sent successfully
            return Response(serializer.data)
        else:
            # SMS sending failed
            # Handle this error according to your application's needs
            return Response({"error": "Failed to send SMS"}, status=500)
