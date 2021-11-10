from rest_framework import serializers
from .models import Group, Groupmember


class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = '__all__'   


class GroupmemberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Groupmember
        fields = '__all__'   