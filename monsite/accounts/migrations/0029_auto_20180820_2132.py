# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-21 01:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_remove_membership_terrain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
