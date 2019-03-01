"""
Django settings for gserv_me project.

Generated by 'django-admin startproject' using Django 2.1.5.

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
SECRET_KEY = 'oa(hiynkjl^p4mz-x+*+6tg5!)a_j6f8ec&ft63s)6h*kq$j#e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

ALLOWED_HOSTS = ["127.0.0.1", "192.168.2.20"]


# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'base.apps.BaseConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'captcha',
    'crispy_forms',

    'django_crispy_bulma',
    'django_simple_bulma',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gserv_me.urls'

TEMPLATES = [
    {
        'APP_DIRS': True,
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],

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

WSGI_APPLICATION = 'gserv_me.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
WHITENOISE_ROOT = os.path.join(STATIC_ROOT, '_')

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django_simple_bulma.finders.SimpleBulmaFinder',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Settings for django-crispy-forms

CRISPY_ALLOWED_TEMPLATE_PACKS = (
    "bootstrap",
    "uni_form",
    "bootstrap3",
    "bootstrap4",
    "bulma",
)

CRISPY_TEMPLATE_PACK = "bulma"


# Settings for django-simple-bulma

BULMA_SETTINGS = {
    "extensions": [
        # Layout extensions
        "bulma-divider",

        # Form extensions
        "bulma-checkradio",
        "bulma-iconpicker",
        "bulma-slider",
        "bulma-switch",
        "bulma-tagsinput",

        # Element extensions
        "bulma-badge",
        "bulma-tooltip",

        # Component extensions
        "bulma-steps",

        # Bundled extensions
        "bulma-fileupload",
        "bulma-navbar-burger",
        "bulma-notifications",
    ],
    "variables": {
        "primary": "#7289DA",

        # "navbar-padding-vertical": "0",
        #
        # "navbar-background-color": "#7289DA",
        # "navbar-item-color": "#C7D0F2",
        #
        # "navbar-item-hover-color": "#C7D0F2",
        # "navbar-item-hover-background-color": "#647BCE",
        #
        # "navbar-item-active-color": "#C7D0F2",
        # "navbar-item-active-background-color": "#647BCE",

        "navbar-padding-vertical": "0",

        "navbar-background-color": "#7289DA",
        "navbar-item-color": "#C7D0F2",

        "navbar-item-hover-color": "#C7D0F2",
        "navbar-item-hover-background-color": "rgba(0, 0, 0, 0.1)",

        "navbar-item-active-color": "#C7D0F2",
        "navbar-item-active-background-color": "rgba(0, 0, 0, 0.2)",
    }
}
