from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_extensions.db.models import ActivatorModel, TimeStampedModel
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
from accountsapp.models import UserProfile


class Chef(ActivatorModel, TimeStampedModel):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="chef_profile")
    # name = models.CharField(max_length=40, null=False, blank=False, default="")
    imageId = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    professional_experience = models.IntegerField()

    def __str__(self):
        return self.user_profile.auth_user.first_name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
