"""
Django settings for dr_backend project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
from django.core.exceptions import ImproperlyConfigured
import json

# JSON-based secrets module
with open('/usr/local/secret/dianarice/db.json') as f:
    secrets = json.load(f)

def get_secret(setting, secrets=secrets):
    '''Get the secret variable or return explicit exception.''' 
    try: 
        return secrets[setting]
    except KeyError: 
        error_msg = 'Set the {0} environment, variable'.format(setting) 
        raise ImproperlyConfigured(error_msg) 

SECRET_KEY = get_secret('SECRET_KEY')

DB_USER = get_secret('DATABASE_USER')
DB_NAME = get_secret('DATABASE_NAME')
DB_PW = get_secret('DATABASE_PASSWORD')
_MEDIA_URL = get_secret("MEDIAURL")
_MEDIA_ROOT = get_secret("MEDIAROOT")
_STATIC_URL = get_secret("STATICURL")
_STATIC_ROOT = get_secret("STATICROOT")
EMAILHOST = get_secret("EMAILHOST")
EMAILUSER = get_secret("EMAILUSER")
SMTPPORT = get_secret("SMTPPORT")
EMAILPASSWORD = get_secret("EMAILPASSWORD")
MAILGUNAPIKEY = get_secret("MAILGUNAPIKEY")
DEFAULTEMAILUSER = get_secret("DEFAULTEMAILUSER")
STRIPEKEY = get_secret("STRIPEKEY")
TWILIOKEY = get_secret("TWILIOKEY")
SMSSENDNUMBER = get_secret("SMSSENDNUMBER")
SMSFROMNUMBER = get_secret("SMSFROMNUMBER")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'adminsortable2',
    # 'anymail',
    'corsheaders',
    'artwork', # activate the new app,
    'carousel',
    'frontend',
    'about',
    'home',
    'sketchbook',
    'rest_framework',
    'rest_framework.authtoken',
    'versatileimagefield',
    # 'frontend', # enable he frontend
    # 'checkout',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dr_backend.urls'

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

WSGI_APPLICATION = 'dr_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PW,
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = _STATIC_URL
   
STATIC_ROOT = _STATIC_ROOT 

MEDIA_ROOT = _MEDIA_ROOT

MEDIA_URL = _MEDIA_URL

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    "http://127.0.0.1:3000",
    "http://stage.dianarice.art",
    "https://stage.dianarice.art",
    "https://media.dianarice.art",
    "https://dianarice.art",
    "https://www.dianarice.art"
]

VERSATILEIMAGEFIELD_SETTINGS = {
    # The amount of time, in seconds, that references to created images
    # should be stored in the cache. Defaults to `2592000` (30 days)
    'cache_length': 2592000,
    # The name of the cache you'd like `django-versatileimagefield` to use.
    # Defaults to 'versatileimagefield_cache'. If no cache exists with the name
    # provided, the 'default' cache will be used instead.
    'cache_name': 'versatileimagefield_cache',
    # The save quality of modified JPEG images. More info here:
    # https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#jpeg
    # Defaults to 70
    'jpeg_resize_quality': 80,
    # The name of the top-level folder within storage classes to save all
    # sized images. Defaults to '__sized__'
    'sized_directory_name': '__sized__',
    # The name of the directory to save all filtered images within.
    # Defaults to '__filtered__':
    'filtered_directory_name': '__filtered__',
    # The name of the directory to save placeholder images within.
    # Defaults to '__placeholder__':
    'placeholder_directory_name': '__placeholder__',
    # Whether or not to create new images on-the-fly. Set this to `False` for
    # speedy performance but don't forget to 'pre-warm' to ensure they're
    # created and available at the appropriate URL.
    'create_images_on_demand': True,
    # A dot-notated python path string to a function that processes sized
    # image keys. Typically used to md5-ify the 'image key' portion of the
    # filename, giving each a uniform length.
    # `django-versatileimagefield` ships with two post processors:
    # 1. 'versatileimagefield.processors.md5' Returns a full length (32 char)
    #    md5 hash of `image_key`.
    # 2. 'versatileimagefield.processors.md5_16' Returns the first 16 chars
    #    of the 32 character md5 hash of `image_key`.
    # By default, image_keys are unprocessed. To write your own processor,
    # just define a function (that can be imported from your project's
    # python path) that takes a single argument, `image_key` and returns
    # a string.
    'image_key_post_processor': None,
    # Whether to create progressive JPEGs. Read more about progressive JPEGs
    # here: https://optimus.io/support/progressive-jpeg/
    'progressive_jpeg': False
}

VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    'image_gallery': [
        ('gallery_large', 'thumbnail__800x600'),
        ('gallery_medium', 'thumbnail__400x300'),
        ('gallery_square_small', 'crop__50x50'),
        ('medium_square_crop', 'crop__400x400'),
        ('gallery_medium_thumbnail', 'thumbnail__600x400'),
        ('original', 'url')
    ],
    'carousel_gallery' : [
         ('gallery_large', 'thumbnail__800x600'),
         ('gallery_medium_thumbnail', 'thumbnail__600x400'),
         ('original', 'url')
    ]
}

ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "MAILGUN_API_KEY": MAILGUNAPIKEY,
    "MAILGUN_SENDER_DOMAIN": EMAILHOST,  # your Mailgun domain, if needed
}

EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
DEFAULT_FROM_EMAIL = 'admin@oh-joy.org'
SERVER_EMAIL = 'admin@oh-joy.org'
EMAIL_HOST = EMAILHOST
EMAIL_PORT = SMTPPORT
EMAIL_HOST_USER = EMAILUSER
EMAIL_HOST_PASSWORD = EMAILPASSWORD
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

