from django.conf import settings 
from django.shortcuts import render
from django.http import HttpResponseRedirect
from.utils import exchange_code_for_token,get_user_info
import uuid
def login(request):
    # Define the redirect URI and state
    redirect_uri = 'http://localhost:8000/api/authorization/callback'  # Replace with your actual redirect URI
    state = uuid.uuid4().hex  # Generate a random state

    # Construct the Okta authorization URL
    auth_url = f"{settings.OIDC_OP_AUTHORIZATION_ENDPOINT}?response_type=code&client_id={settings.OIDC_RP_CLIENT_ID}&redirect_uri={redirect_uri}&scope=openid&state={state}"

    # Redirect to the Okta authorization URL
    print(auth_url)
    # context = {'auth_url': auth_url}
    # return render(request, 'base.html', context)
    return HttpResponseRedirect(auth_url)

def home(request):
    return render(request, 'home.html')

def callback(request):
    # Exchange the authorization code for a token
    token = exchange_code_for_token(request.GET.get('code'))
    
    # Get the user info from Okta
    user_info = get_user_info(token)

    # Create or update the user in Django
    # ...
    # print(user_info)
    # Redirect the user to the desired page
    # return HttpResponseRedirect(reverse('home'))
    context = {'token': token, 'user_info': user_info}
    return render(request, 'home.html', context)
