"""
For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# from django.conf.global_settings import DEFAULT_FROM_EMAIL # using .env instead of this

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.getenv("SECRET_KEY")
SECRET_KEY = 'django-insecure-=5bso*air5)$)%$$g-g*5=z8l*bd=aflu(cc%(ox9vsyji+j&#'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

CELERY_BROKER_URL = "redis://localhost:6379"  # 'redis-10049.c100.us-east-1-4.ec2.cloud.redislabs.com:10049'#
CELERY_RESULT_BACKEND = "redis://localhost:6379"  # 'redis-10049.c100.us-east-1-4.ec2.cloud.redislabs.com:10049'#
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
ROOT_URLCONF = 'gamers_pool.urls'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'  # - без проверки
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory' #Приветственное письмо вновьзарегистрировавшемуся товарищу
# Для установки этого значения "mandatory" требуется ACCOUNT_EMAIL_REQUIRED быть True.
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"  # все уведомления будут приходить в консоль.
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'#Чтобы уведомления приходили на почту

SITE_ID = 1

ACCOUNT_FORMS = {"signup": "sign.models.BasicSignupForm"}

# EMAIL_HOST = os.getenv("EMAIL_HOST")
# EMAIL_PORT = os.getenv("EMAIL_PORT")
# EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")  # mail.ru пароль для внешнего приложения
# DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")

EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 2525
EMAIL_HOST_USER = 'vasinvladimir@inbox.ru'
EMAIL_HOST_PASSWORD = '2548s3hVzkmenZfjnqnM'
DEFAULT_FROM_EMAIL = 'vasinvladimir@inbox.ru'

EMAIL_USE_SSL = False
EMAIL_USE_TLS = True

ADMINS = {'admin', 'skippervasin@gmail.com'}

SERVER_EMAIL = DEFAULT_FROM_EMAIL

# Application definition

INSTALLED_APPS = [
    'modeltranslation',  # транслятор д.б. перед админом
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'main',
    'sign',
    'protect',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.google',
    "django_apscheduler",  # отправлять периодические письма

    'sorl.thumbnail', # Работа с картинками
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.middleware.locale.LocaleMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

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

                'django.template.context_processors.request',  # `allauth` needs this from django
            ],
        },
    },
]

WSGI_APPLICATION = 'gamers_pool.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru'
LANGUAGES = [
    ('ru', 'Русский'),
    ('en-us', 'English')
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
SITE_URL = "http://127.0.0.1:8000"


STATICFILES_DIRS = [BASE_DIR, "main/static", ]
STATIC_URL = '/static/'
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
