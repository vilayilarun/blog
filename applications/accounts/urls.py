#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('sign-up/', views.SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]
