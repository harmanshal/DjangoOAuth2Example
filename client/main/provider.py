from social_core.backends.oauth import BaseOAuth2


class DjangoOAuthToolkitBackend(BaseOAuth2):
    name = 'django'
    AUTHORIZATION_URL = 'http://127.0.0.1:8000/oauth/authorize/'
    ACCESS_TOKEN_URL = 'http://127.0.0.1:8000/oauth/token/'
    ACCESS_TOKEN_METHOD = 'POST'


