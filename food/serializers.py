
from .models import *
from rest_framework import serializers


class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ["id", "name"]


class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = ["id", "name"]


class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = ["id", "name", "imageId", "bio", "pickup_location"]


class PaymentMethodSupportedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethodSupported
        fields = ["cash_on_pickup", "cash_on_delivery"]