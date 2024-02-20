import requests
from django.conf import settings


def exchange_code_for_token(code):
    # Exchange the authorization code for a token
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://localhost:8000/api/authorization/callback',
        'client_id': settings.OIDC_RP_CLIENT_ID,
        'client_secret': settings.OIDC_RP_CLIENT_SECRET,
    }
    response = requests.post(settings.OIDC_RP_TOKEN_ENDPOINT, data=data)
    if response.status_code ==  200:
        return response.json()
    else:
        # Handle the error case, e.g., log the error or raise an exception
        raise Exception(f"Failed to exchange code for token: {response.text}")


def get_user_info(token):
    # Get the user info from Okta
    headers = {'Authorization': f'Bearer {token["access_token"]}'}
    response = requests.get(settings.OIDC_OP_USER_ENDPOINT, headers=headers)
    return response.json()