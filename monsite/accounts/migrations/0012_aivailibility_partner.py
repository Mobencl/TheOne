# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-30 15:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20180727_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='aivailibility',
            name='partner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.ProfileUser'),
        ),
    ]