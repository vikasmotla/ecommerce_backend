from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

PAYMENT_STATUS = (
    ('created' , 'created'),
    ('success' , 'success'),
    ('failed' , 'failed'),
)

PAYMENT_CHANNEL = (
    ('cod','cod'),
    ('upi' , 'upi'),
    ('paytm' , 'paytm'),
    ('ebs' , 'ebs'),
    ('paypal' , 'paypal'),
    ('card' , 'card'),
    ('net_banking' , 'net_banking'),
    ('wallet' , 'wallet'),
    ('other' , 'other'),
)

class Payment(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    paid_amount = models.FloatField(default = 0.0) #this is amount paid via cash or online or wallet #this can be used for refund amount as well
    reference_id = models.CharField(null = False, max_length=150)
    payment_status = models.CharField(choices = PAYMENT_STATUS , max_length = 30 , default='created')
    payment_channel = models.CharField(choices = PAYMENT_CHANNEL , max_length = 30 , default='cod')

class Wallet(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    wallet_user = models.ForeignKey(User ,null = False, related_name ="wallet_user")
    wallet_amount = models.FloatField(null = True)
    is_active = models.BooleanField(default = True)
