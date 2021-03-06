from rest_framework import serializers

# from food.models import UserProfile
from accountsapp.models import Address


# class ChefSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Chef
#         fields = ["instagram_url", "facebook_url", "imageId", "professional_experience"]
#         # read_only_fields = ['auth_user']

#
# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         # exclude=["status"]
#         fields = ["phone_number", "gender", "instagram_url", "facebook_url"]
#         lookup_field = "auth_user"
#
#
class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "contact_name", "contact_number", "Landmark", "state", "city", "pincode", "is_primary"]
        # exclude = ('auth_user', )
