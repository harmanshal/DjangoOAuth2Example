import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-gr5(f&_g8bi6$y355u(c6p#ys83!t4*^45+i(jfa($83b=ljng'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Сторонние пакеты
    'rest_framework',
    'drf_spectacular',

    # OAuth
    'oauth2_provider',
    'social_django',
]

LOGIN_URL = 'social/login/django/'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

OAUTH2_PROVIDER = {
    'RESOURCE_SERVER_INTROSPECTION_URL': 'http://provider-nginx:8000/oauth/introspect/',
    'RESOURCE_SERVER_INTROSPECTION_CREDENTIALS': (
        os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET')
    )
}

AUTHENTICATION_BACKENDS = (
    "main.oauth_backend.DjangoOAuthToolkitBackend",
    "django.contrib.auth.backends.ModelBackend"
)


OAUTH2_BACKEND = {
    # todo: Проблемы со спец символами
    'CLIENT_ID': 'self',
    'CLIENT_SECRET': 'self',
    'AUTHORIZATION_URL': 'http://127.0.0.1:8000/oauth/authorize/',
    'ACCESS_TOKEN_URL': 'http://provider-nginx:8000/oauth/token/',
    'USER_DETAILS_URL': 'http://provider-nginx:8000/api/users/me/'
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SESSION_COOKIE_NAME = 'clientsessionid'

SPECTACULAR_SETTINGS = {
    'TITLE': 'OAuth 2.0 Client API',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
    'SCHEMA_PATH_PREFIX': '/api/',

    # Oauth2 related settings. used for example by django-oauth2-toolkit.
    # https://spec.openapis.org/oas/v3.0.3#oauthFlowsObject
    'OAUTH2_FLOWS': [
        'password'
    ],
    'OAUTH2_AUTHORIZATION_URL': 'http://127.0.0.1:8000/oauth/authorize/',
    'OAUTH2_TOKEN_URL': 'http://127.0.0.1:8000/oauth/token/',
    'OAUTH2_REFRESH_URL': None,
    'OAUTH2_SCOPES': None,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
