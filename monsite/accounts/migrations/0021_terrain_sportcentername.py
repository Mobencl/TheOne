# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-12 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20180806_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='terrain',
            name='sportcenterName',
            field=models.CharField(default='', max_length=255),
        ),
    ]
