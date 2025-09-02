"""
Django settings for the railway project.
Modernized for Django 4.2+ and a Docker environment.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Core Settings ---

# SECURITY WARNING: It's a best practice to load the secret key from an environment variable.
SECRET_KEY = os.getenv('SECRET_KEY', 'h!_@k=ec%#ahh)vfx^r-ljl_n%%y4wd5(3tuouth)-0s+g(0_#')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Allows the Django app to respond to requests within the Docker network.
ALLOWED_HOSTS = ["*"]


# --- Application Definition ---

INSTALLED_APPS = [
    'reservation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'railway.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Add your app's template directory to this list
        'DIRS': [
            BASE_DIR / 'reservation' / 'templates',
        ],
        'APP_DIRS': True, # Keep this as True
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'railway.wsgi.application'


# --- Database Configuration ---

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# --- Password Validation ---

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# --- Internationalization ---

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# --- Static & Media Files ---

# URL to use when referring to static files located in STATIC_ROOT.
STATIC_URL = '/static/'
# Directory where Django will collect all static files for production.
STATIC_ROOT = BASE_DIR / 'staticfiles'
# Additional locations the staticfiles app will traverse.
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = '/media/'
# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = BASE_DIR / 'media'


# --- Default Primary Key Field Type ---

# Use BigAutoField as the default type for auto-created primary keys.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'