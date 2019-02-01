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

class CouponCodeViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny ,)
    serializer_class = CouponCodeSerializer
    queryset = CouponCode.objects.all()

class TrackingLogViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny ,)
    serializer_class = TrackingLogSerializer
    queryset = TrackingLog.objects.all()

class OrderedProductViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny ,)
    serializer_class = OrderedProductSerializer
    queryset = OrderedProduct.objects.all()

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny ,)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class CartViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny ,)
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

class SavedProductViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny ,)
    serializer_class = SavedProductSerializer
    queryset = SavedProduct.objects.all()
