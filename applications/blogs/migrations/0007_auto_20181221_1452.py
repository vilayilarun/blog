# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-21 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20181221_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
