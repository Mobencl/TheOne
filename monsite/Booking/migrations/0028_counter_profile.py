# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-24 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0039_auto_20180821_2303'),
        ('Booking', '0027_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.ProfileUser'),
        ),
    ]