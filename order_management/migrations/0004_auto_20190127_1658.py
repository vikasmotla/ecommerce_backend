# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-27 11:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0003_order_amount_paid_by_wallet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='couponcode',
            old_name='active',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_cancellable',
            new_name='is_cancellable',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_cancelled',
            new_name='is_cancelled',
        ),
        migrations.RenameField(
            model_name='orderedproduct',
            old_name='cancellable',
            new_name='is_cancellable',
        ),
        migrations.RenameField(
            model_name='orderedproduct',
            old_name='cancelled',
            new_name='is_cancelled',
        ),
    ]
