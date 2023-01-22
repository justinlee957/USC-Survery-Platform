"""
Django settings for elcform project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# TODO: replace this with a unique, unpredictable value
SECRET_KEY = 'django-insecure-i&kex6#udp^l0s-lst34mwqpeuj&i!=3a=fre4lv#7*e=1=kq9'
# TODO: replace this with a unique, unpredictable value
HASHID_FIELD_SALT = 'c9Lrync^SeeZ8qP2hVoK#@XnD&M6jY&N'

# SECURITY WARNING: don't run with debug turned on in production!
# TODO: change this to False before deploying
DEBUG = True

# TODO: add the domain name here
# e.g. ALLOWED_HOSTS = ['example.com']
ALLOWED_HOSTS = []

# TODO: add https://your-domain-name here
# e.g. CSRF_TRUSTED_ORIGINS = ['https://example.com']
CSRF_TRUSTED_ORIGINS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'debug_toolbar',
    'survey'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'elcform.urls'

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

WSGI_APPLICATION = 'elcform.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# TODO: change this to connect to production database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# TODO: consider setting HTTP Strict Transport Security header
# after you finish deploying the backend. 
# 
# Warning: Setting this incorrectly can irreversibly (for some time) break your
#          site. Set this after you are sure things work.
# https://docs.djangoproject.com/en/4.0/ref/middleware/#http-strict-transport-security

# SECURE_HSTS_SECONDS = 31536000 # 31536000 sec = 1 year

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'django-static/'
# TODO: set STATIC_ROOT based on the webserver configuration
# STATIC_ROOT = '/var/www/html/django-static'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '60/minute',
        'user': '60/minute'
    },
    'VIEW_DESCRIPTION_FUNCTION': 'elcform.view_description.get_view_description',
    'DEFAULT_PAGINATION_CLASS': 'elcform.pagination.DefaultLimitOffsetPagination'
}

INTERNAL_IPS = [
    "127.0.0.1",
]


# dj_rest_auth
REST_USE_JWT = True
REST_SESSION_LOGIN = False

# Fixes Django Debug Toolbar disallowed MIME type (“text/plain”) on Windows
import mimetypes
mimetypes.add_type("application/javascript", ".js", True)