from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from ..services.AdmiralService import AdmiralService
from ..services.MstService import MstService
from .common import create_response


@require_POST
def get_option_setting(request):
    admiralData = AdmiralService.get_admiral_by_id(2005354) or {}
    api_data = {
        "api_skin_id": admiralData.get("api_skin_id", 0),
        "api_volume_setting": admiralData.get("api_volume_setting", 0),
    }

    return create_response(api_data)


@require_POST
def getData(request):
    api_mst_bgm = MstService.get_mst_bgm()
    api_data = {
        "api_mst_bgm": api_mst_bgm,
        # "api_mst_const": admiralData.get("api_volume_setting", 0),
        # "api_mst_equip_exslot": admiralData.get("api_volume_setting", 0),
        # "api_mst_equip_exslot_ship": admiralData.get("api_volume_setting", 0),
        # "api_mst_equip_limit_exslot": admiralData.get("api_volume_setting", 0),
        # "api_mst_equip_ship": admiralData.get("api_volume_setting", 0),
        # "api_mst_furniture": admiralData.get("api_volume_setting", 0),
        # "api_mst_item_shop": admiralData.get("api_volume_setting", 0),
        # "api_mst_maparea": admiralData.get("api_volume_setting", 0),
        # "api_mst_mapbgm": admiralData.get("api_volume_setting", 0),
        # "api_mst_mapinfo": admiralData.get("api_volume_setting", 0),
        # "api_mst_mission": admiralData.get("api_volume_setting", 0),
        # "api_mst_payitem": admiralData.get("api_volume_setting", 0),
        # "api_mst_ship": admiralData.get("api_volume_setting", 0),
        # "api_mst_shipgraph": admiralData.get("api_volume_setting", 0),
        # "api_mst_shipupgrade": admiralData.get("api_volume_setting", 0),
        # "api_mst_slotitem": admiralData.get("api_volume_setting", 0),
        # "api_mst_slotitem_equiptype": admiralData.get("api_volume_setting", 0),
        # "api_mst_stype": admiralData.get("api_volume_setting", 0),
        # "api_mst_useitem": admiralData.get("api_volume_setting", 0),
    }

    return create_response(api_data)
