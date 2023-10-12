import requests
from django.conf import settings
from social_core.backends.oauth import BaseOAuth2


class DjangoOAuthToolkitBackend(BaseOAuth2):
    name = 'django'
    AUTHORIZATION_URL = settings.OAUTH2_BACKEND['AUTHORIZATION_URL']
    ACCESS_TOKEN_URL = settings.OAUTH2_BACKEND['ACCESS_TOKEN_URL']
    USER_DETAILS_URL = settings.OAUTH2_BACKEND['USER_DETAILS_URL']
    ACCESS_TOKEN_METHOD = 'POST'

    def get_user_details(self, response):
        resp = requests.get(self.USER_DETAILS_URL, headers={
            'Authorization': f'Bearer {response["access_token"]}',
        })

        resp.raise_for_status()

        user_details = resp.json()
        user_details['fullname'] = user_details['first_name'] + ' ' + user_details['last_name']

        return user_details

    def get_key_and_secret(self):
        """Return tuple with Consumer Key and Consumer Secret for current
        service provider. Must return (key, secret), order *must* be respected.
        """
        return settings.OAUTH2_BACKEND['CLIENT_ID'], settings.OAUTH2_BACKEND['CLIENT_SECRET']





