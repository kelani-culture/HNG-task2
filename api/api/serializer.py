from rest_framework import serializers
from .models import User
import re

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'name']
    
    
    def validate_name(self, data):
        result = re.match(r"^[a-zA-Z]+$", data)
        if not result:
            raise serializers.ValidationError("Invalid name")
        
        return data