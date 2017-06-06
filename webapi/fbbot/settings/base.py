"""
Django settings for Facebook Interface for Quizzler project.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import pathlib

# Init dotenv.
from quizzler import env    # noqa


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)
)))

# Development settings.
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

DEBUG = False

ALLOWED_HOSTS = []

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']


# Application definition

DATABASES = {}

INSTALLED_APPS = [
    'fbbot',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'fbbot.middlewares.CommitDatabaseMiddleware',
]

ROOT_URLCONF = 'webapi.fbbot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                    os.path.join(BASE_DIR, 'templates').replace('\\', '/'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
            ],
        },
    },
]

WSGI_APPLICATION = 'webapi.wsgi.app'


# Logging.
# This logs everything to stderr by default.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {    # Match access log style.
            'format': '[%(asctime)s] "%(levelname)s %(name)s" %(message)s',
            'datefmt': r'%d/%b/%Y %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': 0,
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'root': {
        'level': 0,
        'handlers': ['console'],
    }
}


# Custom settings.

FACEBOOK_ACCESS_TOKEN = os.environ['FACEBOOK_ACCESS_TOKEN']
FACEBOOK_VERIFY_TOKEN = os.environ['FACEBOOK_VERIFY_TOKEN']


del os
del pathlib
