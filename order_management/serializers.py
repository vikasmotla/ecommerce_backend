from django.contrib.auth.models import User , Group
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import *
from .models import *
from rest_framework.response import Response

class CouponCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponCode
        fields = ('pk', 'created', 'updated' ,'code_name','min_order_amount','valid_from','valid_till','valid_count','discount_perc','is_active')

class TrackingLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingLog
        fields = ('pk', 'created', 'updated' , 'logTxt')

class OrderedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedProduct
        fields = ('pk', 'created', 'updated' , 'product','product_quantity','paid_amount','product_amount','status','is_cancellable','is_cancelled','additional_notes','discount_perc','tracking_log')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('pk', 'created', 'updated' , 'user','total_amount','order_tracking_id','ordered_products','coupon_code','discount_perc','additional_notes','is_cancellable','is_cancelled','shipment_address','billing_address','payment_details')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('pk', 'created', 'updated' , 'user','product','quantity','typ')

class SavedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedProduct
        fields = ('pk', 'created', 'updated' , 'user','product')
