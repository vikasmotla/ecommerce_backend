from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from .models import *
from .serializers import *
from rest_framework import viewsets , permissions , serializers
from url_filter.integrations.drf import DjangoFilterBackend
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny ,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny ,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

class AddressViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny ,)
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
