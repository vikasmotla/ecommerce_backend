# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-27 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='couponcode',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
