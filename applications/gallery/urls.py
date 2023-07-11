#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path, include

from django.contrib.auth.decorators import login_required

from .views import GalleryView

urlpatterns = [
    path('', (GalleryView.as_view()), name='gallery'),
]
