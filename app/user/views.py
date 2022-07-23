"""
Views for the user API.
"""
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# RetireveUpdateAPIView is provided by Django-rest framework for updating
# and retrieving object in Database.
class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    # specify How are we authenticating user
    authentication_classes = [authentication.TokenAuthentication]
    # The user that uses this API needs to be autheticated already.
    permission_classes = [permissions.IsAuthenticated]

    # Overriding the existing method
    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user
