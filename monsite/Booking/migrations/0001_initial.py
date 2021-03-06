# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-31 23:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0016_auto_20180731_1941'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('bookingFrom', models.DateTimeField(blank=True, null=True)),
                ('bookingUntil', models.DateTimeField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('booking_id', models.CharField(default=uuid.UUID('c76e04a0-d2db-49f6-b994-76cc31541eb1'), max_length=254)),
                ('terraintype', models.CharField(max_length=254)),
                ('terrain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Terrain')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
