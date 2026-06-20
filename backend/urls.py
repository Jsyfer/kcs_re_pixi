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
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

from .views import (
    initialize,
    api_start2,
    api_req_member,
    api_get_member,
    api_port,
    api_req_kaisou,
    api_req_hensei,
    api_req_hokyu,
    test_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", initialize.index, name="index"),
    path("favicon.ico", initialize.favicon, name="favicon"),
    path("img/<path:path>", initialize.send_assets, name="send_assets"),
    path("resources/<path:path>", initialize.send_assets, name="send_assets"),
    path("imigrate/item_used", test_view.item_used),
    path("kcsapi/api_start2/get_option_setting", api_start2.get_option_setting),
    path("kcsapi/api_start2/getData", api_start2.getData),
    path("kcsapi/api_req_member/get_incentive", api_req_member.get_incentive),
    path("kcsapi/api_req_member/set_oss_condition", api_req_member.set_oss_condition),
    path("kcsapi/api_get_member/require_info", api_get_member.require_info),
    path("kcsapi/api_get_member/preset_deck", api_get_member.preset_deck),
    path("kcsapi/api_get_member/ndock", api_get_member.ndock),
    path("kcsapi/api_get_member/preset_dev_items", api_get_member.preset_dev_items),
    path("kcsapi/api_get_member/chart_additional_info", api_get_member.chart_additional_info),
    path("kcsapi/api_get_member/mapinfo", api_get_member.mapinfo),
    path("kcsapi/api_get_member/ship3", api_get_member.ship3),
    path("kcsapi/api_get_member/preset_slot", api_get_member.preset_slot),
    path("kcsapi/api_port/port", api_port.port),
    path("kcsapi/api_req_hensei/change", api_req_hensei.change),
    path("kcsapi/api_req_kaisou/can_preset_slot_select", api_req_kaisou.can_preset_slot_select),
    path("kcsapi/api_req_kaisou/unsetslot_all", api_req_kaisou.unsetslot_all),
    path("kcsapi/api_req_kaisou/slotset", api_req_kaisou.slotset),
    path("kcsapi/api_req_kaisou/slotset_ex", api_req_kaisou.slotset_ex),
    path("kcsapi/api_req_kaisou/slot_exchange_index", api_req_kaisou.slot_exchange_index),
    path("kcsapi/api_req_kaisou/slot_deprive", api_req_kaisou.slot_deprive),
    path("kcsapi/api_req_kaisou/preset_slot_select", api_req_kaisou.preset_slot_select),
    path("kcsapi/api_req_hokyu/charge", api_req_hokyu.charge),
]

urlpatterns += [
    re_path(
        r"^(?P<path>.*)$",
        serve,
        {"document_root": settings.KCS2_ASSETS_DIR},
    )
]
