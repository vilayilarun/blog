# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-02 15:23
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0015_auto_20181221_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('video', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'About',
            },
        ),
        migrations.CreateModel(
            name='SocialMediaProfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=255)),
                ('profile_link', models.URLField()),
                ('image', models.ImageField(upload_to='')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('about_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_profiles', to='blogs.About')),
            ],
            options={
                'verbose_name': 'Social Media',
            },
        ),
    ]
