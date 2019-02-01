from django.contrib.auth.models import User , Group
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import *
from .models import *
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk','username', 'first_name', 'last_name', 'email', 'last_login', 'is_active', 'is_superuser', 'last_login', 'date_joined', 'is_staff')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('pk','created', 'updated', 'user', 'user_dp', 'user_dob', 'user_gender','user_phone')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('pk','created', 'updated', 'address_user', 'address_line1', 'street', 'city','state','country','landmark','pincode','address_typ')
