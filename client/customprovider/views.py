import requests
from allauth.socialaccount.helpers import render_authentication_error, complete_social_login
from allauth.socialaccount.models import SocialLogin
from allauth.socialaccount.providers.base import AuthError
from allauth.socialaccount.providers.oauth.client import OAuthClient
from allauth.socialaccount.providers.oauth2.client import OAuth2Client, OAuth2Error
from allauth.socialaccount.providers.oauth2.views import (OAuth2Adapter, OAuth2LoginView, OAuth2View,
                                                          OAuth2CallbackView)
from allauth.utils import get_request_param
from urllib.parse import parse_qsl

from .provider import CustomProvider
from django.conf import settings


class CustomClient(OAuth2Client):
    def get_access_token(self, code, pkce_code_verifier=None):
        data = {
            "redirect_uri": self.callback_url,
            "grant_type": "authorization_code",
            "code": code,
        }
        if self.basic_auth:
            auth = requests.auth.HTTPBasicAuth(self.consumer_key, self.consumer_secret)
        else:
            auth = None
            data.update(
                {
                    "client_id": self.consumer_key,
                    "client_secret": self.consumer_secret,
                }
            )
        params = None
        self._strip_empty_keys(data)
        url = 'http://provider-nginx:8000/oauth/token/'
        if self.access_token_method == "GET":
            params = data
            data = None
        if data and pkce_code_verifier:
            data["code_verifier"] = pkce_code_verifier
        # TODO: Proper exception handling
        resp = requests.request(
            self.access_token_method,
            url,
            params=params,
            data=data,
            headers=self.headers,
            auth=auth,
        )

        access_token = None
        if resp.status_code in [200, 201]:
            # Weibo sends json via 'text/plain;charset=UTF-8'
            if (
                    resp.headers["content-type"].split(";")[0] == "application/json"
                    or resp.text[:2] == '{"'
            ):
                access_token = resp.json()
            else:
                access_token = dict(parse_qsl(resp.text))
        if not access_token or "access_token" not in access_token:
            raise OAuth2Error("Error retrieving access token: %s" % resp.content)
        return access_token


class CustomAdapter(OAuth2Adapter):
    provider_id = CustomProvider.id
    client_class = CustomClient

    # Fetched programmatically, must be reachable from container
    access_token_url = '{}/oauth/token/'.format(settings.OAUTH_SERVER_BASEURL)
    profile_url = '{}/profile/'.format(settings.OAUTH_SERVER_BASEURL)

    # Accessed by the user browser, must be reachable by the host
    authorize_url = '{}/oauth/authorize/'.format(settings.OAUTH_SERVER_BASEURL)

    # NOTE: trailing slashes in URLs are important, don't miss it

    def complete_login(self, request, app, token, **kwargs):
        headers = {'Authorization': 'Bearer {0}'.format(token.token)}
        resp = requests.get(self.profile_url, headers=headers)
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request, extra_data)

oauth2_login = OAuth2LoginView.adapter_view(CustomAdapter)
oauth2_callback = OAuth2CallbackView.adapter_view(CustomAdapter)
