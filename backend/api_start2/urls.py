from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from . import views
from pathlib import Path

urlpatterns = [
    path("get_option_setting", views.get_option_setting),
]
