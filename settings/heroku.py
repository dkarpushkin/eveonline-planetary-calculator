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

AWS_S3_SECURE_URLS = False       # use http instead of https
AWS_QUERYSTRING_AUTH = False                # don't add complex authentication-related query parameters for requests
AWS_S3_ACCESS_KEY_ID = os.environ.get('AWS_S3_ACCESS_KEY_ID')
AWS_S3_SECRET_ACCESS_KEY = os.environ.get('AWS_S3_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = "sr-secretary"
AWS_S3_HOST = "s3.amazonaws.com"  # Change to the media center you chose when creating the bucket

DEFAULT_FILE_STORAGE = "sr_secretary.s3utils.MediaS3BotoStorage"
