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

def index(request):
    return render(request , 'index.html' , {'data':''})

class TestViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny ,)
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['abc']

class ProductMediaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny ,)
    serializer_class = ProductMediaSerializer
    queryset = ProductMedia.objects.all()

class CategoryMediaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny ,)
    serializer_class = CategoryMediaSerializer
    queryset = CategoryMedia.objects.all()

class BrandMediaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny ,)
    serializer_class = BrandMediaSerializer
    queryset = BrandMedia.objects.all()

class ProductMetaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny ,)
    serializer_class = ProductMetaSerializer
    queryset = ProductMeta.objects.all()

class BrandViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny ,)
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny ,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ProductAtrributeViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny ,)
    serializer_class = ProductAtrributeSerializer
    queryset = ProductAtrribute.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny ,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
