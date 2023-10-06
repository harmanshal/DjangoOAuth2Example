from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from .views import UserViewSet, index

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('social/', include('social_django.urls'), name='social')
]

urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]
