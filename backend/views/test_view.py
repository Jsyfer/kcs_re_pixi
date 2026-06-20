from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from ..services.AdmiralService import AdmiralService
from ..services.MstService import MstService
from ..services.ShipService import ShipService
from ..services.SlotItemService import SlotItemService
from ..services.AirBaseService import AirBaseService
from .common import create_response, create_response_success
from django.conf import settings


# TODO 初始化迁移数据时使用此方法为装备添加被装备的舰娘列
@require_POST
def item_used(request):
    ship_list = ShipService.get_ship()
    for ship in ship_list:
        # 更新ex装备的被使用舰船
        ex_item_id = ship["api_slot_ex"]
        if ex_item_id != -1 and ex_item_id != 0:
            ex_item = SlotItemService.get_slot_item_by_id(ex_item_id)
            ex_item.api_used_ship = ship["api_id"]
        # 更新装备的被使用舰船
        slot_items = ship["api_slot"]
        for slot_item_id in slot_items:
            if slot_item_id != -1 and slot_item_id != 0:
                slot_item = SlotItemService.get_slot_item_by_id(slot_item_id)
                slot_item.api_used_ship = ship["api_id"]
                slot_item.save()
    # 陆航被使用基地
    air_base_list = AirBaseService.get_air_base()
    for air_base in air_base_list:
        for api_plane in air_base.get("api_plane_info", []):
            air_plane_id = api_plane.get("api_slotid")
            if air_plane_id != -1 and air_plane_id != 0:
                slot_item = SlotItemService.get_slot_item_by_id(air_plane_id)
                slot_item.api_used_air_base = air_base["id"]
                slot_item.save()
    return create_response_success()
