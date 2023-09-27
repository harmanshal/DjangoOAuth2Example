from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework import routers

from main.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]
