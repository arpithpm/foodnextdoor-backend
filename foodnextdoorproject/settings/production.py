from base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('dbname'),
        'USER': os.environ.get('dbuser'),
        'PASSWORD': os.environ.get('dbpwd'),
        'HOST': os.environ.get('dbhost'),
        'PORT': '5432',
    }
}
