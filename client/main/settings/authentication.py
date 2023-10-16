import os

LOGIN_URL = 'social/login/django/'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

AUTHENTICATION_BACKENDS = (
    "main.oauth_backend.DjangoOAuthToolkitBackend",
    "django.contrib.auth.backends.ModelBackend"
)

OAUTH2_BACKEND = {
    'CLIENT_ID': 'r3CuSXmOtHOGn0XWTy1MmmwzT3RI7I0Hu4i6LIqP',
    'CLIENT_SECRET': 'client_secret&%$=',
    'AUTHORIZATION_URL': 'http://127.0.0.1:8000/oauth/authorize/',
    'ACCESS_TOKEN_URL': 'http://provider-nginx:8000/oauth/token/',
    'USER_DETAILS_URL': 'http://provider-nginx:8000/api/users/me/'
}

OAUTH2_PROVIDER = {
    'RESOURCE_SERVER_INTROSPECTION_URL': 'http://provider-nginx:8000/oauth/introspect/',
    'RESOURCE_SERVER_INTROSPECTION_CREDENTIALS': (
        'r3CuSXmOtHOGn0XWTy1MmmwzT3RI7I0Hu4i6LIqP', 'client_secret&%$='
    )
}
