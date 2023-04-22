from rest_framework import serializers
from .models import Reaction, UserPet, Post, Follow

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserPet
        fields = '__all__'
        
        
class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    
    class Meta:
        model = Post
        fields = '__all__'
        
        
class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = '__all__'
        
class ReactionSerializer(serializers.ModelSerializer):
            
    class Meta:
        model = Reaction
        fields = '__all__'
