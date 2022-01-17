from rest_framework import generics
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

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