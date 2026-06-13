from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from ..services.AdmiralService import AdmiralService
from ..services.MstService import MstService
from .common import create_response
from django.conf import settings


# 游戏加载时母港皮肤音量设置获取
@require_POST
def get_option_setting(request):
    admiralData = AdmiralService.get_admiral_by_id(settings.MEMBER_ID) or {}
    api_data = {
        "api_skin_id": admiralData.get("api_skin_id", 0),
        "api_volume_setting": admiralData.get("api_volume_setting", 0),
    }

    return create_response(api_data)


# 游戏加载时master数据获取
@require_POST
def getData(request):
    api_data = {
        "api_mst_bgm": MstService.get_mst_bgm(),
        "api_mst_const": MstService.get_mst_const(),
        "api_mst_equip_exslot": MstService.get_mst_mst_equip_exslot(),
        "api_mst_equip_exslot_ship": MstService.get_mst_mst_equip_exslot_ship(),
        "api_mst_equip_limit_exslot": MstService.get_mst_equip_limit_exslot(),
        "api_mst_equip_ship": MstService.get_mst_equip_ship(),
        "api_mst_furniture": MstService.get_mst_furniture(),
        "api_mst_item_shop": MstService.get_mst_item_shop(),
        "api_mst_maparea": MstService.get_mst_maparea(),
        "api_mst_mapbgm": MstService.get_mst_mapbgm(),
        "api_mst_mapinfo": MstService.get_mst_mapinfo(),
        "api_mst_mission": MstService.get_mst_mission(),
        "api_mst_payitem": MstService.get_mst_payitem(),
        "api_mst_ship": MstService.get_mst_ship(),
        "api_mst_shipgraph": MstService.get_mst_shipgraph(),
        "api_mst_shipupgrade": MstService.get_mst_shipupgrade(),
        "api_mst_slotitem": MstService.get_mst_slotitem(),
        "api_mst_slotitem_equiptype": MstService.get_mst_slotitem_equiptype(),
        "api_mst_stype": MstService.get_mst_stype(),
        "api_mst_useitem": MstService.get_mst_useitem(),
    }

    return create_response(api_data)
