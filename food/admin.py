from django.contrib import admin
from food.models import Cuisine, FoodCategory, Chef

# Register your models here.
admin.site.register([Cuisine, FoodCategory, Chef])