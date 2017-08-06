from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG') is not None and os.environ.get('DEBUG').lower() == 'true'

PLATFORM = 'heroku'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
import dj_database_url

DATABASES = {
    'default': dj_database_url.config()
}

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/



STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
