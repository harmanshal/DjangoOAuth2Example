from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from main.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path(r'^accounts/', include('allauth.urls')),
]
