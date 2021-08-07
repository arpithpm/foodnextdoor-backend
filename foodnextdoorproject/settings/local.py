from base import *
import os
from dotenv import load_dotenv

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# load the environment variables from .env files
load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
