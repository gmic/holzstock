from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['.holzstock.com']
WWW_HOST = "www.holzstock.com"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME', 'holzstock'),
        'USER': os.getenv('DATABASE_USER', 'holzstock'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'holzstock'),
        'HOST': os.getenv('DATABASE_HOST', 'localhost'),
        'PORT': os.getenv('DATABASE_PORT', '5432'),
    }
}