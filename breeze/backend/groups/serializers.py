from rest_framework import serializers
from .models import Group, Groupmember


class GroupmemeberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Groupmember
        fields = '__all__'   