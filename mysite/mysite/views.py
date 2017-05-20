from django.template.loader import get_template
from django.template import RequestContext, loader
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from .forms import AuthenticateForm, RegistrationForm
from django.contrib import auth
from scraper_app.scraper import table_head_data
from django.views.generic.edit import FormView
from django.views.generic.base import View


@login_required(login_url="/login/")
def table(request):
    return render(request, 'table.html', {'tableHead': table_head_data})


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
