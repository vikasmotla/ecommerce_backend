# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-01 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UMS', '0001_initial'),
        ('order_management', '0004_auto_20190127_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addr_billing', to='UMS.Address'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipment_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addr_shipping', to='UMS.Address'),
        ),
    ]
