# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('x', '0003_auto_20151226_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpior2',
            name='toggle_state',
            field=models.CharField(choices=[(b'ON', b'ON'), (b'OFF', b'OFF')], default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='gpior2',
            name='pin',
            field=models.IntegerField(choices=[(2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (19, 19), (18, 18), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27)]),
        ),
    ]
