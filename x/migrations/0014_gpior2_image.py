# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-21 06:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('x', '0013_icon_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpior2',
            name='image',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, to='x.Icon'),
        ),
    ]