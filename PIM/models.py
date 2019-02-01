from __future__ import unicode_literals
from django.db import models
from ecommerce.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Inventory(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    product = models.ForeignKey(Product, null = False, related_name = "inventory_product")
    in_stock = models.PositiveIntegerField(null = False, default = 0)
    is_online = models.BooleanField(default = True)
    is_restricted = models.BooleanField(default = False)

class Reviews(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    product =  models.ForeignKey(Product, null = False , related_name = "review")
    rating =  models.PositiveIntegerField(null = False)
    comment = models.CharField(null = True, max_length = 1000)
    title = models.CharField(null = True, max_length = 100 )
    user = models.ForeignKey(User, null = False, related_name ="rev_user")
