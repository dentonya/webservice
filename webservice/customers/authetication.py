import requests
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User  # Assuming you're using the Django User model
from django.conf import settings

class OktaTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            return None

        # Validate the token with Okta's API
        user = self.validate_token(token)
        if not user:
            raise exceptions.AuthenticationFailed('Invalid token.')

        return user, token

    def validate_token(self, token):
        # Okta Token Introspection Endpoint
        okta_domain = settings.OKTA_DOMAIN
        introspection_endpoint = f'https://{okta_domain}/oauth2/default/v1/introspect'

        # Okta client credentials
        client_id = settings.OIDC_RP_CLIENT_ID
        client_secret = settings.OIDC_RP_CLIENT_SECRET

        # Construct the request payload
        data = {
            'token': token,
            'token_type_hint': 'access_token',
            'client_id': client_id,
            'client_secret': client_secret
        }

        # Make a POST request to the Token Introspection endpoint
        response = requests.post(introspection_endpoint, data=data)

        if response.status_code == 200:
            # Token is valid, handle the response
            token_info = response.json()
            print(token_info)

            # Extract user information from token_info
            user_id = token_info.get('sub')
            if user_id:
                # Assuming you have a User model in your Django project
                user, created = User.objects.get_or_create(username=user_id)
                return user
            else:
                print("No user_id found in token_info.")
                return None
        else:
            # Token is not valid, handle the error
            print(f"Token validation failed: {response.status_code}, {response.text}")
            return None
