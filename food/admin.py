from django.contrib import admin
# from food.models import Cuisine, FoodCategory, Chef
from food.models import *

# Register your models here.
admin.site.register([Cuisine, FoodCategory, Chef, PaymentMethodSupported])