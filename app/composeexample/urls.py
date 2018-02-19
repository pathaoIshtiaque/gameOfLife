from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.contrib import admin
from rest_framework import routers, serializers, viewsets

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls)
]
