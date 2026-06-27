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
    api_req_ranking,
    api_get_member,
    api_port,
    api_req_kaisou,
    api_req_hensei,
    api_req_hokyu,
    test_view,
    api_req_nyukyo,
    api_req_kousyou,
    api_req_practice,
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
    path("kcsapi/api_req_member/updatecomment", api_req_member.updatecomment),
    path("kcsapi/api_req_member/get_practice_enemyinfo", api_req_member.get_practice_enemyinfo),
    path("kcsapi/api_req_ranking/mxltvkpyuklh", api_req_ranking.mxltvkpyuklh),
    path("kcsapi/api_get_member/require_info", api_get_member.require_info),
    path("kcsapi/api_get_member/preset_deck", api_get_member.preset_deck),
    path("kcsapi/api_get_member/ndock", api_get_member.ndock),
    path("kcsapi/api_get_member/kdock", api_get_member.kdock),
    path("kcsapi/api_get_member/preset_dev_items", api_get_member.preset_dev_items),
    path("kcsapi/api_get_member/chart_additional_info", api_get_member.chart_additional_info),
    path("kcsapi/api_get_member/mapinfo", api_get_member.mapinfo),
    path("kcsapi/api_get_member/ship3", api_get_member.ship3),
    path("kcsapi/api_get_member/preset_slot", api_get_member.preset_slot),
    path("kcsapi/api_get_member/material", api_get_member.material),
    path("kcsapi/api_get_member/slot_item", api_get_member.slot_item),
    path("kcsapi/api_get_member/payitem", api_get_member.payitem),
    path("kcsapi/api_get_member/record", api_get_member.record),
    path("kcsapi/api_get_member/practice", api_get_member.practice),
    path("kcsapi/api_get_member/mission", api_get_member.mission),
    path("kcsapi/api_req_practice/change_matching_kind", api_req_practice.change_matching_kind),
    path("kcsapi/api_port/port", api_port.port),
    path("kcsapi/api_req_hensei/change", api_req_hensei.change),
    path("kcsapi/api_req_kaisou/can_preset_slot_select", api_req_kaisou.can_preset_slot_select),
    path("kcsapi/api_req_kaisou/unsetslot_all", api_req_kaisou.unsetslot_all),
    path("kcsapi/api_req_kaisou/slotset", api_req_kaisou.slotset),
    path("kcsapi/api_req_kaisou/slotset_ex", api_req_kaisou.slotset_ex),
    path("kcsapi/api_req_kaisou/slot_exchange_index", api_req_kaisou.slot_exchange_index),
    path("kcsapi/api_req_kaisou/slot_deprive", api_req_kaisou.slot_deprive),
    path("kcsapi/api_req_kaisou/preset_slot_select", api_req_kaisou.preset_slot_select),
    path("kcsapi/api_req_kaisou/preset_slot_register", api_req_kaisou.preset_slot_register),
    path("kcsapi/api_req_kaisou/preset_slot_update_lock", api_req_kaisou.preset_slot_update_lock),
    path("kcsapi/api_req_kaisou/preset_slot_update_name", api_req_kaisou.preset_slot_update_name),
    path("kcsapi/api_req_kaisou/preset_slot_delete", api_req_kaisou.preset_slot_delete),
    path("kcsapi/api_req_kaisou/open_exslot", api_req_kaisou.open_exslot),
    path("kcsapi/api_req_kaisou/powerup", api_req_kaisou.powerup),
    path("kcsapi/api_req_kaisou/remodeling", api_req_kaisou.remodeling),
    path("kcsapi/api_req_kaisou/marriage", api_req_kaisou.marriage),
    path("kcsapi/api_req_hokyu/charge", api_req_hokyu.charge),
    path("kcsapi/api_req_nyukyo/start", api_req_nyukyo.start),
    path("kcsapi/api_req_nyukyo/speedchange", api_req_nyukyo.speedchange),
    path("kcsapi/api_req_kousyou/destroyship", api_req_kousyou.destroyship),
    path("kcsapi/api_req_kousyou/destroyitem2", api_req_kousyou.destroyitem2),
    path("kcsapi/api_req_kousyou/getship", api_req_kousyou.getship),
    path("kcsapi/api_req_kousyou/createship", api_req_kousyou.createship),
    path("kcsapi/api_req_kousyou/createitem", api_req_kousyou.createitem),
    path("kcsapi/api_req_kousyou/createship_speedchange", api_req_kousyou.createship_speedchange),
]

urlpatterns += [
    re_path(
        r"^(?P<path>.*)$",
        serve,
        {"document_root": settings.KCS2_ASSETS_DIR},
    )
]
