"""
Django settings for webservice project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from dotenv import load_dotenv
import dj_database_url
load_dotenv()
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'africastalking',
    'rest_framework',
    # OAuth
    'oauth2_provider',
    'social_django',
    'corsheaders',
    'oidc_provider',
    'orders',
    'customers'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webservice.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'webservice.wsgi.application'



# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#       'default': {
#           'ENGINE': 'django.db.backends.postgresql',
#           'NAME':  os.getenv('DB_NAME'),
#           'USER': os.getenv('DB_USER'),
#           'PASSWORD': os.getenv('DB_PASSWORD'),
#           'HOST': os.getenv('DB_HOST'),
#           'PORT': os.getenv('DB_PORT'),
#       }
#   }

DATABASES = {
      'default': 
          dj_database_url.parse(os.getenv('DATABASE_URL'))

}



OAUTH2_PROVIDER = {
    "OIDC_ENABLED": True,
    "SCOPES": {
        "openid": "OpenID Connect scope",
        "read": 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups',
        # ... any other scopes that you use
    },
    # ... any other settings you want
}
LOGIN_URL = '/admin/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

OKTA_DOMAIN =  os.getenv('OKTA_DOMAIN')
OIDC_RP_CLIENT_ID = os.getenv('OKTA_CLIENTID')
OIDC_RP_CLIENT_SECRET = os.getenv('OKTA_CLIENTSECRET')
OIDC_RP_SIGN_ALGO = "RS256"
OIDC_OP_AUTHORIZATION_ENDPOINT = f"https://{OKTA_DOMAIN}/oauth2/default/v1/authorize" # The OIDC authorization endpoint
OIDC_RP_TOKEN_ENDPOINT = f"https://{OKTA_DOMAIN}/oauth2/default/v1/token" # The OIDC token endpoint
OIDC_OP_USER_ENDPOINT = f"https://{OKTA_DOMAIN}/oauth2/default/v1/userinfo" # The OIDC userinfo endpoint
OIDC_OP_TOKEN_ENDPOINT = f"https://{OKTA_DOMAIN}/oauth2/default/v1/token" # The OIDC token endpoint
OIDC_OP_JWKS_ENDPOINT = f"https://{OKTA_DOMAIN}/oauth2/default/v1/keys" # The OIDC JWKS endpoint


AFRICASTKNG_USERNAME = os.getenv('USER_NAME')
AFRICASTKNG_API_KEY = os.getenv('API_KEY')

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'