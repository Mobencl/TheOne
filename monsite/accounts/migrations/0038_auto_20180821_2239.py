# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-22 02:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_auto_20180821_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='photo',
            field=models.ImageField(default='', upload_to='user_directory_path'),
        ),
        migrations.AlterField(
            model_name='terrain',
            name='photo',
            field=models.ImageField(default='', upload_to='user_directory_path'),
        ),
    ]