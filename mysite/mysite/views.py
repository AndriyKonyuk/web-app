from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from .forms import RegisterForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from scraper_app.scraper import table_head_data
# from scraper_app.task import add_data_to_table



def login(request):
    if request.POST:
        password = request.POST['pass']
        username = request.POST['user']
        user = auth.authenticate(username=username, password=password)

        if user is None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/table')
    return render_to_response('login.html')


def register(request):
    if request.POST:
        username = request.POST['user']
        password = request.POST['pass']
        email = request.POST['email']
        if request.session['user'] == None:
            u = User(user=username, password=password, email=email)
            u.save()
            request.session['user'] = username
        elif request.session['user'] == username:
            HttpResponseRedirect('/login')
    return render(request, 'register.html')

# add_data_to_table()

def table(request):
    if request.user.is_authenticated:
        return render(request, 'table.html', {'tableHead': table_head_data})
    else:
        return HttpResponseRedirect('/login')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/logout")
