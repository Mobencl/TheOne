# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-15 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0013_auto_20180814_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_inprogress',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
