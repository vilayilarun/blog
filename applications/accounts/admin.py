#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from applications.accounts.models import User


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email',
                                         'phone',)}),
    )
    filter_horizontal = ('groups', 'user_permissions', )


admin.site.register(User, UserAdmin)
