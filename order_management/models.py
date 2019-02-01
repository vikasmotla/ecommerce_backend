from __future__ import unicode_literals
from time import time
from django.db import models
from django.contrib.auth.models import User
from ecommerce.models import Product
from UMS.models import Address
from payment.models import Payment



class CouponCode(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    code_name = models.CharField(max_length=100, null = False)
    min_order_amount = models.PositiveIntegerField(null = False)
    valid_from = models.DateTimeField(null = False)
    valid_till = models.DateTimeField(null = False)
    valid_count = models.PositiveIntegerField(null = False)
    discount_perc = models.FloatField(null = False)
    is_active = models.BooleanField(default = True)

class TrackingLog(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    logTxt = models.CharField(max_length = 200, null = True )

ORDERED_PRODUCT_STATUS = (
    ('created' , 'created'),
    ('packed' , 'packed'),
    ('shipped' , 'shipped'),
    ('inTransit' , 'inTransit'),
    ('reachedNearestHub' , 'reachedNearestHub'),
    ('outForDelivery' , 'outForDelivery'),
    ('delivered' , 'delivered'),
    ('cancelled' , 'cancelled'),
    ('returned' , 'returned'),
)

class OrderedProduct(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    product = models.ForeignKey(Product, null = False, related_name = "ordered_product")
    product_quantity = models.PositiveIntegerField(null = False)
    paid_amount = models.FloatField(default = 0.0)
    product_amount = models.FloatField(null = False)
    status = models.CharField(choices = ORDERED_PRODUCT_STATUS , max_length = 30 , default='created' )
    is_cancellable = models.BooleanField(default = True)
    is_cancelled = models.BooleanField(default = False)
    additional_notes =  models.CharField(max_length=500, null = True)
    discount_perc = models.FloatField(default = 0.0) # particular prod discount
    tracking_log = models.ManyToManyField(TrackingLog, related_name='trackLogs', blank=True)

PAYMENT_TYPES = (
    ('cod','cod'),
    ('card','card'),
    ('upi','upi'),
    ('paypal','paypal'),
    ('paytm','paytm'),
)

PAYMENT_STATUS = (
    ('created' , 'created'),
    ('failed' , 'failed'),
    ('completed' , 'completed'),
)

class Order(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User ,null = False, related_name ="order_user")
    total_amount = models.FloatField(null = False)
    order_tracking_id = models.CharField(max_length=100 ,null = False)
    ordered_products = models.ManyToManyField(OrderedProduct , related_name='order_products')
    coupon_code = models.ForeignKey(CouponCode ,null = True , related_name ="order_coupon")
    discount_perc = models.FloatField(default = 0.0)
    additional_notes = models.CharField(max_length=500, null = True)
    is_cancellable = models.BooleanField(default = True)
    is_cancelled = models.BooleanField(default = False)
    shipment_address = models.ForeignKey(Address ,null = True , related_name ="addr_shipping")
    billing_address = models.ForeignKey(Address ,null = True , related_name ="addr_billing")
    payment_details = models.ForeignKey(Payment, null = True, related_name = "payment")

CART_TYPE_CHOICES = (
    ('cart' , 'cart'),
    ('wishlist' , 'wishlist'),
)

class Cart(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User ,null = False, related_name ="cart_user")
    product = models.ForeignKey(Product, null = False, related_name = "cart_product")
    quantity = models.PositiveIntegerField(null = False)
    typ = models.CharField(choices = CART_TYPE_CHOICES , max_length = 10 , default = 'cart')

class SavedProduct(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User ,null = False, related_name ="saved_user")
    product = models.ForeignKey(Product, null = False, related_name = "saved_product")
