# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-01 16:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('amount', models.FloatField(default=0.0)),
                ('reference_id', models.CharField(max_length=150)),
                ('payment_status', models.CharField(choices=[('success', 'success'), ('failed', 'failed'), ('other', 'other')], default='other', max_length=30)),
                ('payment_channel', models.CharField(choices=[('upi', 'upi'), ('paytm', 'paytm'), ('ebs', 'ebs'), ('paypal', 'paypal'), ('card', 'card'), ('net_banking', 'net_banking'), ('other', 'other')], default='other', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('wallet_amount', models.FloatField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('wallet_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallet_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
