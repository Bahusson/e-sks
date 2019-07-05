"""
Django settings for esks project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd_vld%wq4fpu1pn*8)x)itbt++-^dn$s60p4dg2y*dk$@^^9#+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Wyłącz debugowanie po wrzuceniu na server w pliku config.

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'akademik.apps.AkademikConfig',
    'rekruter.apps.RekruterConfig',
    'strona.apps.StronaConfig',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Kolejność tego draństwa jest ważna.
# https://docs.djangoproject.com/en/2.2/topics/cache/#order-of-middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


]

ROOT_URLCONF = 'esks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'esks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'esksdb',
        'USER': 'postgres',
        'PASSWORD': 'Mu3kata!owieC',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

# CACHE bazodanowy. https://docs.djangoproject.com/en/2.2/topics/cache/
# Przed użyciem stwórz tabelę w bazie danych za pomocą: "python manage.py createcachetable"
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
        'TIMEOUT': 10,
        'OPTIONS': {
            'MAX_ENTRIES': 2000,
            'CULL_FREQUENCY': 2
        }
    }
}

CACHE_MIDDLEWARE_ALIAS = 'default'

CACHE_MIDDLEWARE_SECONDS = 10

CACHE_MIDDLEWARE_KEY_PREFIX = ''

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
# Dla sesji opartych na ciastkach "django.contrib.sessions.backends.signed_cookies"

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Moduł tłumaczeniowy, jak wszystko z MODELTRANSLATION w nazwie
# https://django-modeltranslation.readthedocs.io/en/latest/
# klasy są tak poustawiane, że dodanie lub usunięcie języka z settings.py
# automatycznie powoduje ich dodanie/usunięcie wszędzie indziej.
# TODO: Poprawić langjs.js żeby też był z tym zsynchronizowany.
gettext = lambda s: s
LANGUAGES = (
    ('pl', gettext('Polish')),  # Pierwszy jest zawsze defaultem chyba, że zrobisz override.
    ('en', gettext('English')),
    ('de', gettext('German')),
    ('fr', gettext('French')),
    ('ru', gettext('Russian')),
    ('uk', gettext('Ukrainian')),
    ('es', gettext('Spanish')),
    ('hi', gettext('Hindi')),
)

LANGUAGE_COOKIE_AGE = 31449600  # Około rok ważności ustawień między logowaniami w sekundach.
# Ustaw None jeśli chcesz, żeby się zerowały po każdym wyłączeniu przeglądarki.

LANGUAGE_COOKIE_NAME = 'esks_language' # Nazwa ciacha językowego, żeby się nie myliło.

LANGUAGE_COOKIE_PATH = '/' # Domyślna ścieżka ciastków. Na wypadek jakbyśmy chcieli nimi manipulować.

MODELTRANSLATION_DEFAULT_LANGUAGE = 'pl' # Tu możesz zmienić default language.

MODELTRANSLATION_LANGUAGES = ('pl', 'en', 'de', 'fr', 'ru', 'uk', 'es', 'hi')

# W ten sposób zachowają sie języki jak nie znajdzie się jakiegoś w bazie. Do zmiany być może?
MODELTRANSLATION_FALLBACK_LANGUAGES = {'default': ('en', ), 'en': ('pl', )}

# Tutaj rejestruje się wszystkie trackery translacyjne translation.py, które umieszczasz w folderze apki.
MODELTRANSLATION_TRANSLATION_FILES = (
    'rekruter.translation',
    'strona.translation',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'esks/static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = '/'  # Przekierowanie usera po zalogowaniu
# jeśli nie masz tego zdefiniowanego inaczej. My mamy, ale zostawiam bo w razie
# "w" default przekierowuje na nieistniejącą stronę. To już lepiej na główną!

LOGOUT_REDIRECT_URL = '/'  # Przekierowanie po wylogowaniu.

# Ściągnij ustawienia lokalne gdybyśmy chcieli udostępnić kod i wejść na OpenSource
# na serwerze obok "settings" robisz plik .local_settings i ustalasz od nowa:
# SECRET_KEY, DEBUG = False, DATABASES, oraz CACHES jeśli używasz Memccache.
try:
    from .local_settings import *
except ImportError:
    pass
