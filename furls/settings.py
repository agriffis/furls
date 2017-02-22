"""
Django settings for furls project.
"""

import os
from bienvenue import make_env_reader
import dj_database_url
from envbash import load_envbash

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Where are we?
DREAMHOST = 'dreamhost' in open('/etc/resolv.conf').read()
DEVELOPMENT = not DREAMHOST

# Load env.bash
if DREAMHOST:
    load_envbash(os.path.expanduser('~/env.bash'))
elif DEVELOPMENT:
    load_envbash(os.path.join(BASE_DIR, 'env.bash'), missing_ok=True)

# Make an env reader to convert strings to inferred types
env = make_env_reader(prefix='DJANGO_')

# This is the dev key, should always be overridden in production.
SECRET_KEY = env('SECRET_KEY', 'vb^%dw%9$1z1bwxia$ednmoc+6uyn**^m@362p$6h-oed7o=8y')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', DEVELOPMENT)

ALLOWED_HOSTS = env('ALLOWED_HOSTS', [])


# Application definition

INSTALLED_APPS = [
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

ROOT_URLCONF = 'furls.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'furls.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://postgres:postgres@postgres/postgres',
        conn_max_age=60,
    ),
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
