import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from oauth2_provider.decorators import protected_resource
from rest_framework import permissions, viewsets

from main.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]


@protected_resource(scopes=['read'])
def profile(request):
    return HttpResponse(json.dumps({
        "id": request.resource_owner.id,
        "username": request.resource_owner.username,
        "email": request.resource_owner.email,
        "first_name": request.resource_owner.first_name,
        "last_name": request.resource_owner.last_name
    }), content_type="application/json")
