from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True

# Easier to read SQL in dev
INSTALLED_APPS += ['django_extensions']