"""
Django settings for codebox project.

Generated by 'django-admin startproject' using Django 4.0.3.

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
SECRET_KEY = 'django-insecure-6759&toh$n1a)$yazxo#7y^u3!0m9ibe72%^m$ktwbw#r$8+rj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
    "django_filters",
    "rest_framework_mongoengine",
    "django_celery_results",
    "django_celery_beat",
    "channels",

    "user",
    "cmdb",
    "jumpserver",
    "common",
    "iac",
    "chat",
    "k8s",
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

ROOT_URLCONF = 'codebox.urls'

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

WSGI_APPLICATION = 'codebox.wsgi.application'
ASGI_APPLICATION = "codebox.asgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'codebox',
        'USER': 'yc',
        'PASSWORD': 'xxx',
        'HOST': 'node02',
        'PORT': '3306',
        'TEST': {
            'NAME': 'mytestdatabase',
        },
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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/
LANGUAGE_CODE = 'zh-Hans' # 'en-us'

TIME_ZONE = 'Asia/Shanghai'  # 'UTC'

USE_I18N = True

USE_TZ = True

USE_DEPRECATED_PYTZ = True

DJANGO_CELERY_BEAT_TZ_AWARE = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    # 异常处理
    # 'EXCEPTION_HANDLER': 'utils.exceptions.global_exception_handler',
    # 'EXCEPTION_HANDLER': 'goldfish.utils.exceptions.custom_exception_handler',
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "DEFAULT_PAGINATION_CLASS": "common.paginations.CustomPageNumberPagination",
    # "DEFAULT_PAGINATION_CLASS": "goldfish.utils.paginations.CustomPageNumberPagination",
    # "DEFAULT_PAGINATION_CLASS": "assistant.pagination.StandardResultSetPagination",
    "PAGE_SIZE": 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'common.auth.BearerTokenAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
}

SPECTACULAR_SETTINGS = {
    "TITLE": "goldfish API",
    "DESCRIPTION": "A simple api",
    "VERSION": "1.0.0",
    "SCHEMA_PATH_PREFIX": "^/api/",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "displayOperationId": True,
    },
}

PAGE_SIZE_QUERY_PARAM = "size"
MAX_PAGE_SIZE = 200
# ansible work dir
WORK_DIR = "/Users/zyc/Desktop/tmp/work"

import os

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        # 'django.db.backends': {
        #     'handlers': ['console'],
        #     'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        #     'propagate': False,
        # },
    },
}


import datetime
# JWT_AUTH = {
#     # jwt的有效期
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
#     # 自定义响应数据格式
#     'JWT_RESPONSE_PAYLOAD_HANDLER': 'users.utils.jwt_response_payload_handler',
# }

SIMPLE_JWT = {
    # jwt的有效期
    # 'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=60),
}

# AUTHENTICATION_BACKENDS = [
#     'users.utils.UsernameMobileAuthBackend',
# ]

MEDIA_ROOT = Path("/Users/zyc/Desktop/tmp")
IAC_WORK_DIR = Path("/Users/zyc/Desktop/tmp/work")

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://node01:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "xxx",
        }
    },
    # 提供给xadmin或者admin的session存储
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://node01:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "xxx",
        }
    },
    "celery": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://node01:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "xxx",
        }
    },
}

# celery
CELERY_RESULT_BACKEND = "django-cache"
CELERY_CACHE_BACKEND = "celery"
CELERY_BROKER_URL = "redis://:xxx@node01:6379/1"
CELERY_TASK_ROUTES = {
    "iac.tasks.*" : {"queue": "iac-1"},
    "k8s.tasks.*" : {"queue": "k8s-1"},
    "jumpserver.tasks.*" : {"queue": "jumpserver-1"},
}



CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            # "hosts": [("node01", 6379)],
            "hosts": ["redis://:xxx@node01:6379/0",],
        },
    },
}

# k8s模板执行目录
TEMPLATE_DIR = "/Users/zyc/PycharmProjects/goldfish/k8s/k8s-files/template/hello-minikube"


MONGODB_DATABASES = {
    "name": "cmdb",
    "host": "node02",
    "port": 27017,
    "tz_aware": True,
    "username": "xxx",
    "password": "xxx"
}

JUMPSERVER_UPLOADS_DIR = BASE_DIR / "upload"
