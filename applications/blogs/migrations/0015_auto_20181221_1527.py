# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-21 15:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0014_blog_gallery_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='blogs.Blog'),
        ),
    ]
