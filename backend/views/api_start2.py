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
    api_data = {
        "api_mst_bgm": MstService.get_mst_bgm(),
        "api_mst_const": {
            "api_boko_max_ships": {"api_string_value": "", "api_int_value": 740},
            "api_dpflag_quest": {"api_string_value": "", "api_int_value": 1},
            "api_parallel_quest_max": {"api_string_value": "", "api_int_value": 10},
        },
        "api_mst_equip_exslot": [16, 21, 23, 27, 28, 36, 39, 43, 44],
        # "api_mst_equip_exslot_ship": admiralData.get("api_volume_setting", 0),
        "api_mst_equip_limit_exslot": {
            "100": [27],
            "101": [27],
            "114": [27],
            "200": [27],
            "290": [27],
            "395": [27],
            "511": [27],
            "512": [27],
            "513": [27],
            "516": [27],
            "574": [27],
            "995": [27],
            "1000": [27],
            "1001": [27],
            "1006": [27],
        },
        # "api_mst_equip_ship": admiralData.get("api_volume_setting", 0),
        "api_mst_furniture": MstService.get_mst_furniture(),
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
