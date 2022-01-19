from rest_framework import generics
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from django.db import IntegrityError
from rest_framework import serializers

from .serializers import *
from .permissions import IsChefOrReadOnly

class CuisineListCreateView(generics.ListCreateAPIView):
    serializer_class = CuisineSerializer
    permission_classes = [IsChefOrReadOnly]
    queryset = Cuisine.objects.active()

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class FoodCategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = FoodCategorySerializer
    permission_classes = [IsChefOrReadOnly]
    queryset = FoodCategory.objects.active()

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class ChefListView(generics.ListAPIView):
    serializer_class = ChefSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Chef.objects.active()


class PaymentMethodSupportedCreateView(generics.CreateAPIView):
    serializer_class = PaymentMethodSupportedSerializer
    permission_classes = [IsChefOrReadOnly]

    def perform_create(self, serializer):
        chef = get_object_or_404(Chef, user=self.request.user)
        try:
            serializer.save(chef=chef)
        except IntegrityError:
            raise serializers.ValidationError("You have already added payment method.")


# class PaymentMethodSupported(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = PaymentMethodSupportedSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = PaymentMethodSupported.objects.all()

#     def get_object(self):
#         chef = get_object_or_404(Chef, user=self.request.user)
#         return get_object_or_404(PaymentMethodSupported, chef=chef)