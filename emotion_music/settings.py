"""
Django settings for emotion_music project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = os.path.abspath('/home/emotion/media')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r*^*mlwgknm5+u0rb+0rs8-&ch&&0xcip@^ii!g3ne8kl)&+5n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "39.117.188.179", "61.77.183.72", "119.196.113.64", "3.35.114.47"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Faceapp',
    'bootstrap4',
    'embed_video',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_elasticsearch_dsl',
]

ELASTICSEARCH_DSL = {
    'default' : {
            'hosts' : '52.199.47.215:9200'
        },
}

LOGGING = {
    'version' : 1,
    'disable_existing_loggers' : False,
    'formatters' : {
        'simple' : {
                'format' : 'velname)s %(message)s'
        },
    },
    'handlers' : {
        'console' : {
            'level' : 'INFO',
            'class' : 'logging.StreamHandler',
            'formatter' : 'simple'
            },
        'logstash' : {
            'level' : 'INFO',
            'class' : 'logstash.TCPLogstashHandler',
            'host' : '52.199.47.215',
            'port' : 5044,
            'version' : 1,
            'message_type' : 'django',
            'fqdn' : False,
            'tags' : ['django.request'],
            },
        },
    'loggers' : {
            'django.request' : {
                    'handlers' : ['logstash'],
                    'level' : 'INFO',
                    'propagate' : True,
                },
            'django' : {
                    'handlers' : ['console', 'logstash'],
                    'propagate' : True,
                },
        }
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'emotion_music.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
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

WSGI_APPLICATION = 'emotion_music.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = { 
	'default': 
	{ 
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'dbteam1', 
    'USER': 'team2', 
    'PASSWORD': 'Team1!2@9(', 
    'HOST': '0.0.0.0', 
    'PORT': '3306',
        }
}



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'


USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
# STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
