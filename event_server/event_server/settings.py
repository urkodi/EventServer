import environ
import sys
import os
from pathlib import Path
from django.db import connections
from django.db.utils import OperationalError

BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize environ - MUST be at the top before using env()
env = environ.Env()
environ.Env.read_env()

# Security & Configuration
SECRET_KEY = env('DJANGO_SECRET_KEY')
DEBUG = env.bool('DEBUG', default=True)

# Stripe Configuration
STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
STRIPE_PUBLISHABLE_KEY = env('STRIPE_PUBLISHABLE_KEY')


ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Custom Apps
    'users.apps.UsersConfig',
    'events.apps.EventsConfig',
    'payments.apps.PaymentsConfig', 
    #Third Party Apps
    'corsheaders',
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # MOVED: Must be before CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'event_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


CORS_ALLOWED_ORIGINS = [
    env("FRONTEND_URL", default="http://localhost:5173"),
]


APPEND_SLASH = False

WSGI_APPLICATION = 'event_server.wsgi.application'

# Database
DATABASES = {
    'default': env.db(),
}

def test_database_connection():
    try: 
        db_conn = connections['default']
        with db_conn.cursor() as cursor:
            cursor.execute("Select 1")
            result = cursor.fetchone()
            print("Database Connected")
    except OperationalError as e:
        print("Database Not Connected")


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

if 'runserver' in sys.argv or 'test' in sys.argv:
    test_database_connection()

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
}