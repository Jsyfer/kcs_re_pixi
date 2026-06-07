from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("initial_loading", views.send_initial_loading, name="initial_loading"),
    path("favicon.ico", views.favicon, name="favicon"),
    path("kcs2/<path:path>", views.send_assets, name="send_assets"),
    path("api/<path:path>", views.send_kcsapi, name="send_kcsapi"),
    path("kcsapi/<path:path>", views.send_kcsapi_request, name="send_kcsapi_request"),
]
