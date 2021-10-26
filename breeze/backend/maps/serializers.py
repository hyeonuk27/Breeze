from rest_framework import serializers
from .models import Place

class PlaceListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Place
        fields = '__all__'