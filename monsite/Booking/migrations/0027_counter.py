# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-24 13:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0026_auto_20180824_0759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(default=0)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.Guest')),
            ],
        ),
    ]
