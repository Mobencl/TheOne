# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-10 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0008_auto_20180807_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='terrain',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AddField(
            model_name='booking_inprogress',
            name='status',
            field=models.CharField(default='Not confirmed', max_length=254),
        ),
        migrations.AlterField(
            model_name='booking_inprogress',
            name='booking_id',
            field=models.CharField(default=uuid.UUID('ee05db4d-5d17-4e46-922e-d7923ca21206'), max_length=254),
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
