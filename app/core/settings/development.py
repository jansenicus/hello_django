from os import getenv
from pathlib import Path
from dotenv import load_dotenv
from .base import *
# Load .env.development
load_dotenv(dotenv_path=BASE_DIR / '.env.development')

SECRET_KEY = getenv('SECRET_KEY', 'fallback-dev-secret')
DEBUG = getenv('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = getenv('ALLOWED_HOSTS', 'localhost').split(',')
# print(f"Allowed hosts for DEVELOPMENT: {ALLOWED_HOSTS}")
DATABASES = {
    'default': {
        'ENGINE': getenv('DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': getenv('DB_NAME', BASE_DIR / 'db.sqlite3'),
        'USER': getenv('DB_USER', ''),
        'PASSWORD': getenv('DB_PASSWORD', ''),
        'HOST': getenv('DB_HOST', ''),
        'PORT': getenv('DB_PORT', ''),
    }
}

AUTH_PASSWORD_VALIDATORS = []
