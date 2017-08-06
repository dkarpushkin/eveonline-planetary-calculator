from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG') is not None and os.environ.get('DEBUG').lower() == 'true'

SECRET_KEY = os.environ["SECRET_KEY"]

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
import dj_database_url

DATABASES = {
    'default': dj_database_url.config("DATABASE_URL"),
    'eve_db': dj_database_url.config("HEROKU_POSTGRESQL_WHITE_URL"),
}

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
