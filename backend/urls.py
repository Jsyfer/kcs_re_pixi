"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve

# from . import views
from .views import get_option_setting, initialize

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_ROOT = Path(BASE_DIR) / "frontend"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", initialize.index, name="index"),
    # path("initial_loading", views.send_initial_loading, name="initial_loading"),
    path("favicon.ico", initialize.favicon, name="favicon"),
    path("img/<path:path>", initialize.send_assets, name="send_assets"),
    path("resources/<path:path>", initialize.send_assets, name="send_assets"),
    path(
        "kcsapi/api_start2/get_option_setting",
        get_option_setting.get_option_setting,
        name="get_option_setting",
    ),
]

urlpatterns += [
    re_path(
        r"^(?P<path>.*)$",
        serve,
        {"document_root": FRONTEND_ROOT},
    )
]
