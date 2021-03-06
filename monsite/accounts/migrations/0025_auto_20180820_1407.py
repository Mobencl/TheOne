# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-20 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_membership'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='terrain',
            name='sportcenterName',
        ),
        migrations.AddField(
            model_name='membership',
            name='partner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.ProfileUser'),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='sportcenterName',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='membership',
            name='status',
            field=models.IntegerField(default=3),
        ),
    ]
