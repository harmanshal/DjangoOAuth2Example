import os

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
