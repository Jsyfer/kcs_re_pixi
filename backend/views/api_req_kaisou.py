from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.forms.models import model_to_dict
from ..services.ShipService import ShipService
from ..services.SlotItemService import SlotItemService
from ..services.MstService import MstService
from ..services.PresetService import PresetService
from .common import create_response, create_response_success
from ..utils import gameUtils


# check是否可以选择编成预设
@require_POST
def can_preset_slot_select(request):
    # TODO : Implement actual logic to determine if preset slot selection is allowed
    api_data = {"api_flag": 1}

    return create_response(api_data)


# 取下所有装备
@require_POST
def unsetslot_all(request):
    api_id = int(request.POST.get("api_id"))
    # 获取舰娘
    ship = ShipService.get_ship_by_id(api_id)
    # 更新舰娘api_slot
    (ship.api_slot or [])[:] = [-1] * len(ship.api_slot or [])
    gameUtils.update_ship_status_with_slot_items(ship)
    ship.save()
    return create_response_success()


# 更换装备
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


# 更换EX装备
@require_POST
def slotset_ex(request):
    api_id = int(request.POST.get("api_id"))
    api_item_id = int(request.POST.get("api_item_id"))
    # 获取舰娘
    ship = ShipService.get_ship_by_id(api_id)
    # 更新舰娘exslot装备
    ship.api_slot_ex = api_item_id
    gameUtils.update_ship_status_with_slot_items(ship)
    ship.save()
    return create_response_success()


# 更换装备位置
@require_POST
def slot_exchange_index(request):
    api_id = int(request.POST.get("api_id"))
    api_src_idx = int(request.POST.get("api_src_idx"))
    api_dst_idx = int(request.POST.get("api_dst_idx"))
    # 获取舰娘
    ship = ShipService.get_ship_by_id(api_id)
    # 更换装备位置
    (ship.api_slot or [])[api_src_idx] = (ship.api_slot or [])[api_dst_idx]
    (ship.api_slot or [])[api_dst_idx] = (ship.api_slot or [])[api_src_idx]
    ship.save()
    api_data = {"api_ship_data": model_to_dict(ship)}
    return create_response(api_data)


# 从其它舰娘身上获取装备
@require_POST
def slot_deprive(request):
    api_unset_idx = int(request.POST.get("api_unset_idx"))
    api_set_slot_kind = int(request.POST.get("api_set_slot_kind"))
    api_unset_slot_kind = int(request.POST.get("api_unset_slot_kind"))
    api_unset_ship = int(request.POST.get("api_unset_ship"))
    api_set_idx = int(request.POST.get("api_set_idx"))
    api_set_ship = int(request.POST.get("api_set_ship"))
    # 获取舰娘
    set_ship = ShipService.get_ship_by_id(api_set_ship)
    unset_ship = ShipService.get_ship_by_id(api_unset_ship)
    # 更新舰娘api_slot对应位置装备
    (set_ship.api_slot or [])[api_set_idx] = (unset_ship.api_slot or [])[api_unset_idx]
    gameUtils.update_ship_status_with_slot_items(set_ship)
    set_ship.save()
    (unset_ship.api_slot or [])[api_unset_idx] = -1
    gameUtils.update_ship_status_with_slot_items(unset_ship)
    unset_ship.save()
    api_data = {
        "api_ship_data": {
            "api_set_ship": model_to_dict(set_ship),
            "api_unset_ship": model_to_dict(unset_ship),
        },
        "api_unset_list": {"api_slot_list": [], "api_type3No": 1},
    }
    return create_response(api_data)


# 展开装备编程预设
@require_POST
def preset_slot_select(request):
    api_preset_id = int(request.POST.get("api_preset_id"))
    api_ship_id = int(request.POST.get("api_ship_id"))
    # TODO handle equip mode 1 or 2(matches A or B on page)
    api_equip_mode = int(request.POST.get("api_equip_mode"))

    # 获取预设装备
    preset_slot_item = PresetService.get_preset_slot_by_id(api_preset_id).api_slot_item or []
    preset_slot_item_ex = PresetService.get_preset_slot_by_id(api_preset_id).api_slot_item_ex
    # 获取舰船
    ship = ShipService.get_ship_by_id(api_ship_id)
    # 更新ex装备
    if preset_slot_item_ex is not None:
        unset_slot_item = SlotItemService.get_unset_slot_item_by_id(preset_slot_item_ex["api_id"])
        if unset_slot_item is not None:
            if ship.api_slot_ex != -1:
                old_exslot_item = SlotItemService.get_slot_item_by_id(ship.api_slot_ex)
                old_exslot_item.api_used_ship = -1
                old_exslot_item.save()
            ship.api_slot_ex = unset_slot_item.api_id
            unset_slot_item.save()
    # 设置旧装备为未使用
    for item_id in ship.api_slot or []:
        if item_id != -1:
            old_slot_item = SlotItemService.get_slot_item_by_id(item_id)
            old_slot_item.api_used_ship = -1
            old_slot_item.save()
    # 卸下全部装备
    (ship.api_slot or [])[:] = [-1] * len(ship.api_slot or [])
    # 更新舰娘api_slot
    for i, mst_item in enumerate(preset_slot_item):
        mst_item_id = mst_item["api_id"]
        unset_slot_item = SlotItemService.get_unset_slot_item_by_id(mst_item_id)
        if unset_slot_item is not None:
            (ship.api_slot or [])[i] = unset_slot_item.api_id
            unset_slot_item.api_used_ship = api_ship_id
            unset_slot_item.save()
    gameUtils.update_ship_status_with_slot_items(ship)
    ship.save()
    api_data = {}
    return create_response(api_data)
