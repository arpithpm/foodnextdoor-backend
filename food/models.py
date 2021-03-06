from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_extensions.db.models import ActivatorModel, TimeStampedModel
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
from accountsapp.models import Address

#
# class Chef(ActivatorModel, TimeStampedModel):
#     user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="chef_profile")
#     # name = models.CharField(max_length=40, null=False, blank=False, default="")
#     imageId = models.TextField(null=True, blank=True)
#     bio = models.TextField(null=True, blank=True)
#     professional_experience = models.IntegerField()
#
#     def __str__(self):
#         return self.user_profile.auth_user.first_name
#
#     def get_absolute_url(self):
#         return reverse("_detail", kwargs={"pk": self.pk})

class Chef(ActivatorModel, TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name="chef_profile")
    name = models.CharField(max_length=40, null=False, blank=False, default="")
    imageId = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    pickup_location = models.OneToOneField(Address, on_delete=models.PROTECT, related_name="chef_profile")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class PaymentMethodSupported(models.Model):
    cash_on_pickup = models.BooleanField(default=False)
    cash_on_delivery = models.BooleanField(default=False)
    chef = models.OneToOneField(Chef, on_delete=models.PROTECT, related_name="payment_methods")

    def __str__(self):
        return self.chef.user.username

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Cuisine(ActivatorModel, TimeStampedModel):
    name = models.CharField(max_length=40, null=False, blank=False, default="", unique=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cuisine_added_by")
    status = models.IntegerField(default=ActivatorModel.INACTIVE_STATUS, null=False, blank=False, choices=ActivatorModel.STATUS_CHOICES)

    def __str__(self):
        return self.name

class FoodCategory(ActivatorModel, TimeStampedModel):
    name = models.CharField(max_length=40, null=False, blank=False, unique=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="food_category_added_by")
    status = models.IntegerField(default=ActivatorModel.INACTIVE_STATUS, null=False, blank=False, choices=ActivatorModel.STATUS_CHOICES)

    def __str__(self):
        return self.name


