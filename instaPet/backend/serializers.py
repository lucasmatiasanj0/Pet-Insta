from rest_framework import serializers
from .models import UserPet

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserPet
        fields = '__all__'
