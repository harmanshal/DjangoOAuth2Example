import requests
from social_core.backends.oauth import BaseOAuth2


class DjangoOAuthToolkitBackend(BaseOAuth2):
    name = 'django'
    AUTHORIZATION_URL = 'http://127.0.0.1:8000/oauth/authorize/'
    ACCESS_TOKEN_URL = 'http://provider-nginx:8000/oauth/token/'
    USER_CREDENTIALS_URL = 'http://provider-nginx:8000/api/users/me/'
    ACCESS_TOKEN_METHOD = 'POST'

    def get_user_details(self, response):
        resp = requests.get(self.USER_CREDENTIALS_URL, headers={
            'Authorization': f'Bearer {response["access_token"]}',
        })

        resp.raise_for_status()

        user_details = resp.json()
        user_details['fullname'] = user_details['first_name'] + ' ' + user_details['last_name']

        return user_details




