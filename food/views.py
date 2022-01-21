from rest_framework import generics, viewsets, permissions, serializers
from rest_framework.generics import get_object_or_404
from django.db import IntegrityError

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


class PaymentMethodSupportedView(viewsets.ModelViewSet):
    serializer_class = PaymentMethodSupportedSerializer
    permission_classes = [IsChefOrReadOnly]

    def list(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(PaymentMethodSupported, chef__user=self.request.user)

    def perform_create(self, serializer):
        chef = get_object_or_404(Chef, user=self.request.user)
        try:
            serializer.save(chef=chef)
        except IntegrityError:
            raise serializers.ValidationError("You have already added payment method.")

    def get_queryset(self):
        return get_object_or_404(PaymentMethodSupported, chef__user=self.request.user)
