# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-24 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0025_booking_inprogress_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='status',
            field=models.IntegerField(default=3),
        ),
    ]
