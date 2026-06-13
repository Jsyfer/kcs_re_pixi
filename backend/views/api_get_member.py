from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST

from ..services.AdmiralService import AdmiralService
from ..services.FurnitureService import FurnitureService
from ..services.KdockService import KdockService
from ..services.SlotItemService import SlotItemService
from ..services.UnsetslotService import UnsetslotService
from ..services.UseitemService import UseitemService
from ..services.DeckService import DeckService
from ..services.NdockService import NdockService
from ..services.MstService import MstService
from ..services.DeckPortService import DeckPortService
from ..services.ShipService import ShipService
from ..common.gameUtils import get_tyku, get_tp
from .common import create_response
from django.conf import settings


# 玩家数据获取
@require_POST
def require_info(request):
    admiralData = AdmiralService.get_admiral() or {}
    api_data = {
        "api_basic": {
            "api_member_id": admiralData.get("api_member_id"),
            "api_firstflag": admiralData.get("api_firstflag"),
        },
        "api_slot_item": SlotItemService.get_slot_items(),
        "api_unsetslot": UnsetslotService.get_unset_slots(),
        "api_kdock": KdockService.get_kdock(),
        "api_useitem": UseitemService.get_useitem(),
        "api_furniture": FurnitureService.get_furniture(),
        "api_extra_supply": admiralData.get("api_extra_supply"),
        "api_oss_setting": {
            "api_language_type": admiralData.get("api_language_type"),
            "api_oss_items": admiralData.get("api_oss_items"),
        },
        "api_skin_id": admiralData.get("api_skin_id"),
        "api_position_id": admiralData.get("api_position_id"),
    }

    return create_response(api_data)


# 编成预设获取
@require_POST
def preset_deck(request):
    admiralData = AdmiralService.get_admiral() or {}
    api_data = {
        "api_deck": DeckService.get_deck(),
        "api_max_num": admiralData.get("api_max_deck"),
    }
    return create_response(api_data)


# 入渠按钮选择时相关信息获取
@require_POST
def ndock(request):
    api_data = NdockService.get_ndock()
    return create_response(api_data)


# 工厂按钮选择时相关信息获取
@require_POST
def preset_dev_items(request):
    admiralData = AdmiralService.get_admiral() or {}
    api_data = {
        "api_max_num": admiralData.get("api_max_dev_items"),
    }
    return create_response(api_data)


# 母港选择出击按钮时各舰队制空/TP信息获取
@require_POST
def chart_additional_info(request):
    api_deck_param = []
    deck_port = DeckPortService.get_deck_port()
    for deck in deck_port:
        deck_ship_equip_list = []
        deck_ship_list = []
        for ship_id in deck["api_ship"]:
            if ship_id != -1:
                ship = ShipService.get_ship_by_id(ship_id)
                mst_ship = MstService.get_mst_ship_by_id(ship.api_ship_id)
                deck_ship_list.append([ship, mst_ship])
                current_ship_equip_list = []
                for index, slot in enumerate(ship.api_slot or {}):
                    if slot != -1:
                        slot_item = SlotItemService.get_slot_item_by_id(slot)
                        mst_slotitem = MstService.get_mst_slotitem_by_id(
                            slot_item.api_slotitem_id
                        )
                        current_ship_equip_list.append(
                            [slot_item, mst_slotitem, (ship.api_onslot or [])[index]]
                        )
                deck_ship_equip_list.append(current_ship_equip_list)
        # 获取制空值
        seiku_value = get_tyku(deck_ship_equip_list)
        # 获取TP值
        tp_value = get_tp(deck_ship_list, deck_ship_equip_list)
        api_deck_param.append(
            {"api_seiku_value": seiku_value["max"], "api_tp_value": tp_value["s"]}
        )
    api_data = {"api_deck_param": api_deck_param}
    return create_response(api_data)
