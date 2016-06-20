# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('x', '0009_auto_20160417_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperaturesensor',
            name='humidity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='temperaturesensor',
            name='temperature',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]