from .models import *
from rest_framework import serializers

def isChef(request):
    try:
        chef = Chef.objects.get(user=request.user)
        if chef.id:
            return True
    except Chef.DoesNotExist:
        return False
    