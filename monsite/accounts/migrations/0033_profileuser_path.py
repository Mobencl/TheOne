# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-21 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_profileuser_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='path',
            field=models.CharField(default='user_directory_path', max_length=255),
        ),
    ]
