#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path, include

from .views import BlogListView, BlogDetailView, AboutView


urlpatterns = [
    path('', (BlogListView.as_view()), name='blogs'),
    path('blog/(?P<slug>[-\w]+)/', BlogDetailView.as_view(), name='detail'),
    path('about/', AboutView.as_view(), name='about'),
]
