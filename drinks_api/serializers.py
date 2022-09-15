from rest_framework import serializers 
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Drink
        fields = ('id', 'name', 'image', 'ingredients', 'comments', 'likes', 'locationDisplayName', 'address', 'latitude', 'longitude', 'tags') 
