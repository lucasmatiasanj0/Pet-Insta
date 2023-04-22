from rest_framework import generics
from .models import UserPet
from .serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend


class UserList(generics.ListAPIView):
    queryset = UserPet.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
