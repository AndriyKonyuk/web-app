from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet, GroupViewSet
from . import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^regin/', views.register, name='regin'),
    url(r'^table/', views.table, name='table'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^users/', UserViewSet),
    # url(r'^groups/', GroupViewSet),
]