# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-21 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0011_auto_20181221_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='banner_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
