# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-17 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0024_auto_20180816_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_inprogress',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]