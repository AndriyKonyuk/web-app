from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet, GroupViewSet
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^', views.table, name='table'),
]