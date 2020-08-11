from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    url("^", include(("index.urls", "index"), namespace="index",)),
]
