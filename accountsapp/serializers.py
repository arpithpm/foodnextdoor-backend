from rest_framework import serializers

from food.models import UserProfile


# class ChefSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Chef
#         fields = ["instagram_url", "facebook_url", "imageId", "professional_experience"]
#         # read_only_fields = ['auth_user']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        # exclude=["status"]
        fields = ["phone_number", "gender", "instagram_url", "facebook_url"]
        lookup_field = "auth_user"
