from django.contrib.auth.models import User , Group
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import *
from .models import *
from rest_framework.response import Response


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('pk', 'created', 'updated','product','in_stock','is_online','is_restricted' )

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('pk', 'created', 'updated','product','rating','comment','title','user' )
