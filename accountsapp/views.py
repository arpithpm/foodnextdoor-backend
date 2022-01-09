from rest_framework import generics
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

# from accountsapp.serializers import UserProfileSerializer, UserAddressSerializer
# from accountsapp.models import Address, UserProfile
from food.permissions import IsSelf, IsOwnerOrReadOnly


# # Create your views here.
# class UserProfileUpdateView(generics.RetrieveUpdateAPIView):
#     serializer_class = UserProfileSerializer
#     permission_classes = [IsOwnerOrReadOnly]
#     # queryset = UserProfile.objects.all()
#     lookup_field = "auth_user"
#
#     def get_object(self):
#         return get_object_or_404(UserProfile, auth_user=self.request.user)
#
#
# class UserAddressCreateView(generics.CreateAPIView):
#     serializer_class = UserAddressSerializer
#     permission_classes = [IsOwnerOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(auth_user=self.request.user)
#
#
# class UserAddressGetUpdateDeleteView(generics.RetrieveUpdateAPIView):
#     serializer_class = UserAddressSerializer
#     permission_classes = [IsSelf]
#     lookup_field = "auth_user"
#
#     def get_object(self):
#         return get_object_or_404(Address, auth_user=self.request.user)
