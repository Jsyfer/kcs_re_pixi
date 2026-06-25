from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST

from ..services.AdmiralService import AdmiralService
from ..services.DeckService import DeckService
from ..services.FurnitureService import FurnitureService
from ..services.LogService import LogService
from ..services.MaterialService import MaterialService
from ..services.NdockService import NdockService
from ..services.ShipService import ShipService
from .common import create_response
from django.conf import settings


# 进入母港界面时，相关信息获取
@require_POST
def port(request):
    admiralData = AdmiralService.get_admiral() or {}
    material_list = MaterialService.get_material_list()
    api_data = {
        "api_basic": AdmiralService.get_admiral(),
        "api_deck_port": DeckService.get_deck_port(),
        "api_dest_ship_slot": admiralData.get("api_dest_ship_slot"),
        "api_furniture_affect_items": FurnitureService.get_furniture_affect_items(),
        "api_log": LogService.get_log(),
        "api_material": material_list,
        "api_ndock": NdockService.get_ndock(),
        "api_p_bgm_id": admiralData.get("api_p_bgm_id"),
        "api_parallel_quest_count": admiralData.get("api_parallel_quest_count"),
        "api_ship": ShipService.get_ship(),
    }

    return create_response(api_data)
