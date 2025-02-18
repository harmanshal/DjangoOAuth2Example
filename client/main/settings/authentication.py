import os

LOGIN_URL = "social/login/django/"

SOCIAL_AUTH_URL_NAMESPACE = "social"

AUTHENTICATION_BACKENDS = (
    "main.oauth_backend.DjangoOAuthToolkitBackend",
    "django.contrib.auth.backends.ModelBackend",
)

OAUTH2_BACKEND = {
    "CLIENT_ID": "hjQbTqMRD0DTSUxdpAN6Wb0efsUoh99ceFGqYYdq",
    "CLIENT_SECRET": "VUvAtuQco1XRauQ6MkaOO3kuikVm2SzEhSYruH3ZfiLRCQQ6KkvR4GEmXb0APnW2BDrMEXvGF2RQx6x5STRA91kDgbKHYWVJ3EU9U4HGjM1pSUwFrAvGvsPviINbdEdD",
    "AUTHORIZATION_URL": "http://localhost:8000/o/authorize/",
    "ACCESS_TOKEN_URL": "http://localhost:8000/o/token/",
    "USER_DETAILS_URL": "http://localhost:8000/common/api/v1/user/me",
}

OAUTH2_PROVIDER = {
    "RESOURCE_SERVER_INTROSPECTION_URL": "http://localhost:8000/o/introspect/",
    "RESOURCE_SERVER_INTROSPECTION_CREDENTIALS": (
        "hjQbTqMRD0DTSUxdpAN6Wb0efsUoh99ceFGqYYdq",
        "VUvAtuQco1XRauQ6MkaOO3kuikVm2SzEhSYruH3ZfiLRCQQ6KkvR4GEmXb0APnW2BDrMEXvGF2RQx6x5STRA91kDgbKHYWVJ3EU9U4HGjM1pSUwFrAvGvsPviINbdEdD",
    ),
}
