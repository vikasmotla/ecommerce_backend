from django.contrib.auth.models import User , Group
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import *
from .models import *
from rest_framework.response import Response

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('pk', 'abc')

class ProductMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMedia
        fields = ('pk', 'created', 'updated', 'typ', 'attachment')

class CategoryMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMedia
        fields = ('pk', 'created', 'updated', 'typ', 'attachment')

class BrandMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandMedia
        fields = ('pk', 'created', 'updated', 'typ', 'attachment')

class ProductMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMeta
        fields = ('pk', 'created', 'updated', 'taxCode', 'taxRate', 'typ')

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('pk', 'created', 'updated', 'brand_name', 'brand_desc', 'brand_media')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'created', 'updated', 'category_name', 'category_desc', 'category_parent', 'category_media')

class ProductAtrributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAtrribute
        fields = ('pk', 'created', 'updated', 'attribute_name', 'attribute_value', 'attribute_unit')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'created', 'updated', 'product_name', 'product_sku', 'product_price', 'product_weight', 'product_desc', 'product_short_desc', 'product_media', 'product_category', 'product_brand', 'product_meta', 'product_attribute', 'product_disc_perc')
