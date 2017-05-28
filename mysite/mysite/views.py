from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from .forms import AuthenticateForm, RegistrationForm
from django.contrib import auth

from django.views.generic.edit import FormView
from django.views.generic.base import View


class my_login(FormView):
    form_class = AuthenticateForm
    template_name = "login.html"
    success_url = "/table"

    def form_valid(self, form):
        self.user = form.get_user()
        auth.login(self.request, self.user)
        return super(my_login, self).form_valid(form)


class my_register(FormView):
    form_class = RegistrationForm
    template_name = "register.html"
    success_url = '/login'

    def form_valid(self, form):
        form.save()
        return super(my_register, self).form_valid(form)


class my_logout(View):
    def get(self, request):
        auth.logout(request)
        return HttpResponseRedirect("/")
