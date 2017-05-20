from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet, GroupViewSet
from . import views
from django.contrib import admin

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    url(r'^$|^login/', views.my_login.as_view(), name='login'),
    url(r'^logout/', views.my_logout.as_view(), name='logout'),
    url(r'^regin/', views.my_register.as_view(), name='regin'),
    url(r'^table/', views.table, name='table'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^users/', UserViewSet),
    # url(r'^groups/', GroupViewSet),
]