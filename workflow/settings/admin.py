from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'workflow',
        'USER': 'workflowadmin',
        'HOST': 'localhost'
    }
}

SHOW_ADMIN = True