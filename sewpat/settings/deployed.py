# noinspection PyUnresolvedReferences
from os import getenv

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('DJANGO_SECRET_KEY')
DB_PASSWORD = getenv('DATABASE_PASSWORD')

DEBUG = False

ALLOWED_HOSTS = ['.tsango.com', ]

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
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '1000/day',
    }
}
