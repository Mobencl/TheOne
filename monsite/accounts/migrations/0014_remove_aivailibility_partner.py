# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-30 15:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20180730_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aivailibility',
            name='partner',
        ),
    ]
