# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0002_auto_20160709_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='clicks_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='link',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
