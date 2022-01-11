# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, **kwargs):
#     obj, created = UserProfile.objects.get_or_create(auth_user=instance)
#     user_profile = obj
#     user_profile.auth_user = instance
#     user_profile.save()


# # user profile is created after signin up/update for User using User model's post_save method
# class UserProfile(ActivatorModel, TimeStampedModel):
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )
#     auth_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
#     phone_number = models.CharField(max_length=10, null=True, blank=True, default="")
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     instagram_url = models.URLField(null=False, blank=True)
#     facebook_url = models.URLField(null=False, blank=True)
#
#     # is_chef = models.BooleanField(default=False, null=False, blank=False)
#
#     def __str__(self):
#         name = self.auth_user.username
#         if len(name) > 1:
#             return name
#         else:
#             return "No name"
#
#     def get_absolute_url(self):
#         return reverse("_detail", kwargs={"pk": self.pk})


from django.contrib.auth.models import User
from django.db import models
from indian_cities.dj_city import cities

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django_extensions.db.models import ActivatorModel, TimeStampedModel



class Address(ActivatorModel, TimeStampedModel):
    state_choices = (
    ("Andhra Pradesh", "Andhra Pradesh"), ("Arunachal Pradesh ", "Arunachal Pradesh "), ("Assam", "Assam"),
    ("Bihar", "Bihar"), ("Chhattisgarh", "Chhattisgarh"), ("Goa", "Goa"), ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"), ("Himachal Pradesh", "Himachal Pradesh"), ("Jammu and Kashmir ", "Jammu and Kashmir "),
    ("Jharkhand", "Jharkhand"), ("Karnataka", "Karnataka"), ("Kerala", "Kerala"), ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"), ("Manipur", "Manipur"), ("Meghalaya", "Meghalaya"), ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"), ("Odisha", "Odisha"), ("Punjab", "Punjab"), ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"), ("Tamil Nadu", "Tamil Nadu"), ("Telangana", "Telangana"), ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"), ("Uttarakhand", "Uttarakhand"), ("West Bengal", "West Bengal"),
    ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"), ("Chandigarh", "Chandigarh"),
    ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"), ("Daman and Diu", "Daman and Diu"),
    ("Lakshadweep", "Lakshadweep"), ("National Capital Territory of Delhi", "National Capital Territory of Delhi"),
    ("Puducherry", "Puducherry"))

    contact_name = models.CharField(max_length=50, null=False, blank=False)
    contact_number = models.CharField(max_length=10)
    Landmark = models.TextField()
    state = models.CharField(choices=state_choices, max_length=255, null=False, blank=False)
    city = models.CharField(choices=cities, null=False, max_length=20)
    pincode = models.CharField(max_length=8, null=False, blank=False)
    auth_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_address")
    # for now, we are not using this. Wil be used in future.
    is_primary = models.BooleanField(default=False) # if true, then it is primary address)

    # user may have more than one address but only one primary address. So, we need to make sure that only one address is primary address.
    def save(self, *args, **kwargs):
        if self.is_primary:
            Address.objects.filter(auth_user=self.auth_user).update(is_primary=False)
        super().save(*args, **kwargs)


    def __str__(self):
        return str(self.auth_user) + " " + str(self.pincode)
