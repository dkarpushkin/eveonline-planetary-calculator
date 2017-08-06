import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'picalc',
        'USER': 'ubuntu',
        'PASSWORD': 'vagrant',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'eve_db': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'evedb',
        'USER': 'ubuntu',
        'PASSWORD': 'vagrant',
        'HOST': 'localhost',
        # 'PORT': '',
    },
}

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, 'debug.log'),
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'django.db.backends': {
#             'level': 'DEBUG',
#             'handers': ['file'],
#         },
#     },
# }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]