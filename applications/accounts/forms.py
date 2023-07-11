#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from django import forms
from django.contrib.auth import authenticate

from applications.accounts.models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.EmailInput(), required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    def clean_username(self):
        if not self.cleaned_data.get('username'):
            raise forms.ValidationError("Username required")
        data = self.cleaned_data.get('username')
        return data

    def clean_password(self):
        if not self.cleaned_data.get('password'):
            raise forms.ValidationError("password required")
        return self.cleaned_data.get('password')

    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if not user:
            raise forms.ValidationError("invalid credentials")
        return self.cleaned_data


class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(max_length=200, widget=forms.PasswordInput)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=200, widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('email', 'phone', 'username',)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Account already exists")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        print(password, password2)
        if password != password2:
            raise forms.ValidationError('Password not match')
        if len(password and password2) < 8:
            raise forms.ValidationError('Password must be eight characters')
        return password
