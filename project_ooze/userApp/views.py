from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework import viewsets
from userApp.serializers import UserSerializer

from userApp.models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

def home(request):
	return HttpResponse("testing")