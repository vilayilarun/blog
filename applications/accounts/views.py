#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

from django.views import generic
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponse
from django.http import JsonResponse

from applications.accounts.forms import LoginForm, RegisterForm


class LoginView(generic.FormView):
    form_class = LoginForm

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        login(self.request, user)
        return JsonResponse({'status': 'success'})

    def form_invalid(self, form):
        print(form.errors)
        return HttpResponse(json.dumps({'result': {'status': 'form_error', 'errors': form.errors}}),
                            content_type='application/json')


class SignUpView(generic.View):

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            sign_up_form = RegisterForm(request.POST)
            if sign_up_form.is_valid():
                user = sign_up_form.save(commit=False)
                user.email = sign_up_form.cleaned_data['email']
                password = sign_up_form.cleaned_data['password']
                user.set_password(password)
                user.save()
                if user is not None:
                    login(self.request, user)
                    return JsonResponse({'status': 'success'})
                return JsonResponse({'status': 'signup-error'})
            else:
                return HttpResponse(json.dumps({'result': {'status': 'form_error', 'errors': sign_up_form.errors}}),
                                    content_type='application/json')

