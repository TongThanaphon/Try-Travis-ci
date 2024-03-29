from rest_framework import generics,status
from rest_framework.response import Response
from .serializers import UserSerializer, TopicSerializer
from .models import User, Topics

class TopicListCreate(generics.ListCreateAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer