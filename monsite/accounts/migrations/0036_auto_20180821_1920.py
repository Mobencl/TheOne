# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-21 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_auto_20180821_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='path',
            field=models.CharField(default='user_directory_path', max_length=255),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='photo',
            field=models.ImageField(default='', upload_to='user_directory_path'),
        ),
    ]
