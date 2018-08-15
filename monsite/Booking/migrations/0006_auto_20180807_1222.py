# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-07 16:22
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0005_auto_20180806_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_id',
            field=models.CharField(default=uuid.UUID('bde8fe54-d5c9-4480-856f-90fe6e08b115'), max_length=254),
        ),
        migrations.AlterField(
            model_name='booking_inprogress',
            name='booking_id',
            field=models.CharField(default=uuid.UUID('2480969a-6291-4589-bfa4-a0ab879f3022'), max_length=254),
        ),
    ]
