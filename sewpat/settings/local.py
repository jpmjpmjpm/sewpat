# noinspection PyUnresolvedReferences
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-iw*ylk@&)@^)j&rq6!$0uxxhxqpt3l0rwf58g@i)8)x=v0j8d+'
DB_PASSWORD = 'password'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sewpat',
        'USER': 'sewpat',
        'PASSWORD': DB_PASSWORD,
        'HOST': '127.0.0.1',
    }
}

# Define permissions policy for using the APIs
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
