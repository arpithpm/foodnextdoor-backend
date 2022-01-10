from rest_framework import generics
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from accountsapp.serializers import UserAddressSerializer
from accountsapp.models import Address
from accountsapp.permissions import IsSelf, IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, AllowAny


# # Create your views here.
# class UserProfileUpdateView(generics.RetrieveUpdateAPIView):
#     serializer_class = UserProfileSerializer
#     permission_classes = [IsOwnerOrReadOnly]
#     # queryset = UserProfile.objects.all()
#     lookup_field = "auth_user"
#
    # def get_object(self):
    #     return get_object_or_404(UserProfile, auth_user=self.request.user)
#
#
class UserAddressListCreateView(generics.ListCreateAPIView):
    serializer_class = UserAddressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Address.objects.filter(auth_user=user)

    def perform_create(self, serializer):
        serializer.save(auth_user=self.request.user)


class UserAddressGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserAddressSerializer
    permission_classes = [IsSelf]
    queryset = Address.objects.all()
    # lookup_field = "id"

    # def get_object(self):
    #     return get_object_or_404(Address, auth_user=self.request.user)

#
#
# class UserAddressGetUpdateDeleteView(generics.RetrieveUpdateAPIView):
#     serializer_class = UserAddressSerializer
#     permission_classes = [IsSelf]
#     lookup_field = "auth_user"
#
#     def get_object(self):
#         return get_object_or_404(Address, auth_user=self.request.user)
