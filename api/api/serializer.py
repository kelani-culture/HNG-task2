from rest_framework import serializers
from .models import User
import re

class UserSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField()
    class Meta:
        model = User
        fields = ['id', 'name']
    
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['id'] = str(repr['id'])
        return repr