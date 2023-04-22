from rest_framework import generics
from .models import Follow, UserPet, Post
from .serializers import FollowSerializer, UserSerializer, PostSerializer, ReactionSerializer
from django_filters.rest_framework import DjangoFilterBackend


class UserList(generics.ListAPIView):
    queryset = UserPet.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    
class CreateUser(generics.CreateAPIView):
    queryset = UserPet.objects.all()
    serializer_class = UserSerializer
    
    
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class CreatePost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
class FollowList(generics.RetrieveAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id']

    
    
    
    
    
