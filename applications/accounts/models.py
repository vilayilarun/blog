#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from autoslug import AutoSlugField


class User(User):
    slug = AutoSlugField(populate_from='email')

    def __unicode__(self):
        return self.slug

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
