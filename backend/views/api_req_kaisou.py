from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from ..services.ShipService import ShipService
from ..services.SlotItemService import SlotItemService
from ..services.MstService import MstService
from .common import create_response, create_response_success
from ..utils import gameUtils


# check是否可以选择编成预设
@require_POST
def can_preset_slot_select(request):
    # TODO : Implement actual logic to determine if preset slot selection is allowed
    api_data = {"api_flag": 1}

    return create_response(api_data)


# TODO 更换装备
@require_POST
def slotset(request):
    api_id = int(request.POST.get("api_id"))
    api_item_id = int(request.POST.get("api_item_id"))
    api_slot_idx = int(request.POST.get("api_slot_idx"))
    # 获取舰娘
    ship = ShipService.get_ship_by_id(api_id)
    # 更新舰娘api_slot对应位置装备
    (ship.api_slot or [])[api_slot_idx] = api_item_id
    gameUtils.update_ship_status_with_slot_items(ship)
    ship.save()
    return create_response_success()


# TODO 更换EX装备
@require_POST
def slotset_ex(request):
    api_id = request.POST.get("api_id")
    api_item_id = request.POST.get("api_item_id")
    # 更新舰娘api_slot对应位置装备

    # 根据装备属性，重新计算舰娘属性，并更新状态

    return create_response_success()
