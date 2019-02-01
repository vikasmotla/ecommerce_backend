from __future__ import unicode_literals
from time import time
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def getDisplayPicturePath(instance , filename):
    return 'ecommerce/static/media/profile/%s_%s' % (str(time()).replace('.', '_'),filename)

GENDER_CHOICES = (
    ('M' , 'Male'),
    ('F' , 'Female'),
    ('O' , 'Other'),
)

class Profile(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User ,null = False, related_name ="prof_user")
    user_dp = models.ImageField(upload_to = getDisplayPicturePath, null=True)
    user_dob = models.DateField( null= True )
    user_gender = models.CharField(choices = GENDER_CHOICES , default = 'M' , max_length = 6)
    user_phone = models.CharField(null = True , max_length = 14)

ADDR_TYP = (
    ('Work' , 'Work'),
    ('Home' , 'Home'),
    ('Other' , 'Other'),
)

class Address(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    address_user = models.ForeignKey(User ,null = False, related_name ="addr_user")
    address_line1 = models.CharField(null = True , max_length = 30)
    street = models.CharField(null = True , max_length = 30)
    city = models.CharField(null = False , max_length = 30)
    state = models.CharField(null = False , max_length = 30)
    country = models.CharField(null = False , max_length = 30)
    landmark = models.CharField(null = True , max_length = 30)
    pincode = models.CharField(null = False , max_length = 10)
    address_typ = models.CharField(choices = ADDR_TYP , default = 'Home' , max_length = 8)
