# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-27 21:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180727_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileuser',
            name='password',
        ),
    ]
