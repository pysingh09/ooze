from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework import viewsets
from userApp.serializers import UserSerializer, PostSerializer

from userApp.models import User, Post


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer