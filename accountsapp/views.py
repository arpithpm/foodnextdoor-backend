from rest_framework import generics
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from accountsapp.serializers import UserProfileSerializer
from food.models import UserProfile
from food.permissions import IsSelf


# Create your views here.
class UserProfileUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsSelf]
    # queryset = UserProfile.objects.all()
    lookup_field = "auth_user"

    def get_object(self):
        return get_object_or_404(UserProfile, auth_user=self.request.user)
