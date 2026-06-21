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
    # 设置装备为未使用
    gameUtils.update_slotitem_used_by_ship(ship.api_slot, -1)
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
    # 设置旧装备为未使用
    gameUtils.update_slotitem_used_by_ship([(ship.api_slot or [])[api_slot_idx]], -1)
    # 更新舰娘api_slot对应位置装备
    (ship.api_slot or [])[api_slot_idx] = api_item_id
    # 设置新装备使用者为当前舰娘
    gameUtils.update_slotitem_used_by_ship([api_item_id], api_id)
    # 更新舰娘状态
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
    # 设置旧装备为未使用
    gameUtils.update_slotitem_used_by_ship([ship.api_slot_ex], -1)
    # 更新舰娘exslot装备
    ship.api_slot_ex = api_item_id
    # 设置新装备使用者为当前舰娘
    gameUtils.update_slotitem_used_by_ship([api_item_id], api_id)
    # 更新舰娘状态
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
    # 获取装备
    if api_set_slot_kind == 1:
        # 1: ex装备槽位
        set_item_id = set_ship.api_slot_ex
    else:
        # 0: 通常装备槽位
        set_item_id = (set_ship.api_slot or [])[api_set_idx]
    if api_unset_slot_kind == 1:
        # 1: ex装备槽位
        unset_item_id = unset_ship.api_slot_ex
    else:
        # 0: 通常装备槽位
        unset_item_id = (unset_ship.api_slot or [])[api_unset_idx]
    # 更新替换用装备使用者为当前舰娘
    gameUtils.update_slotitem_used_by_ship([unset_item_id], api_set_ship)
    # 更新被替换掉装备使用者为无
    gameUtils.update_slotitem_used_by_ship([set_item_id], -1)
    # 更新舰娘api_slot对应位置装备
    if api_set_slot_kind == 1:
        set_ship.api_slot_ex = unset_item_id
    else:
        (set_ship.api_slot or [])[api_set_idx] = unset_item_id
    gameUtils.update_ship_status_with_slot_items(set_ship)
    set_ship.save()
    # 从该装备原来所属舰娘卸载装备
    if api_unset_slot_kind == 1:
        unset_ship.api_slot_ex = -1
    else:
        (unset_ship.api_slot or [])[api_unset_idx] = -1
    gameUtils.update_ship_status_with_slot_items(unset_ship)
    unset_ship.save()
    api_ship_data = {
        "api_set_ship": model_to_dict(set_ship),
        "api_unset_ship": model_to_dict(unset_ship),
    }

    if set_item_id == -1:
        api_data = {"api_ship_data": api_ship_data}
    else:
        # 更新未设定装备列表
        mst_item_id = SlotItemService.get_slot_item_by_id(set_item_id).api_slotitem_id
        mst_item = MstService.get_mst_slotitem_by_id(mst_item_id)
        api_type = mst_item.api_type[2]  # type: ignore
        api_data = {
            "api_ship_data": api_ship_data,
            "api_unset_list": {
                "api_slot_list": SlotItemService.get_unset_slots()["api_slottype" + str(api_type)],
                "api_type3No": api_type,
            },
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
            # 卸载旧装备
            gameUtils.update_slotitem_used_by_ship([ship.api_slot_ex], -1)
            ship.api_slot_ex = unset_slot_item.api_id
            unset_slot_item.save()
    # 设置旧装备为未使用
    gameUtils.update_slotitem_used_by_ship(ship.api_slot, -1)
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


# 新建装备预设
@require_POST
def preset_slot_register(request):
    api_preset_id = int(request.POST.get("api_preset_id"))
    api_ship_id = int(request.POST.get("api_ship_id"))
    # 获取舰娘
    ship = ShipService.get_ship_by_id(api_ship_id)
    api_slot_item = []
    for slot_item_id in ship.api_slot or []:
        if slot_item_id != -1:
            slot_item = SlotItemService.get_slot_item_by_id(slot_item_id)
            mst_slot_item = MstService.get_mst_slotitem_by_id(slot_item.api_slotitem_id)
            api_slot_item.append(
                {
                    "api_id": mst_slot_item.api_id,
                    "api_level": slot_item.api_level,
                }
            )
    api_slot_item_ex = None
    if ship.api_slot_ex != -1:
        slot_item_ex = SlotItemService.get_slot_item_by_id(ship.api_slot_ex)
        mst_slot_item_ex = MstService.get_mst_slotitem_by_id(slot_item_ex.api_slotitem_id)
        api_slot_item_ex = {
            "api_id": mst_slot_item_ex.api_id,
            "api_level": slot_item_ex.api_level,
        }

    preset = {
        "api_preset_no": api_preset_id,
        "api_name": f"第{api_preset_id:02}",
        "api_selected_mode": 1,
        "api_lock_flag": 0,
        "api_slot_ex_flag": 0,
        "api_slot_item": api_slot_item,
        "api_slot_item_ex": api_slot_item_ex,
    }
    PresetService.create_preset_slot(preset)
    return create_response_success()


# 锁定装备预设
@require_POST
def preset_slot_update_lock(request):
    api_preset_id = int(request.POST.get("api_preset_id"))
    preset = PresetService.get_preset_slot_by_id(api_preset_id)
    preset.api_lock_flag ^= 1
    preset.save()
    return create_response_success()


# 更新装备预设名称
@require_POST
def preset_slot_update_name(request):
    api_preset_id = int(request.POST.get("api_preset_id"))
    api_name = request.POST.get("api_name")
    preset = PresetService.get_preset_slot_by_id(api_preset_id)
    preset.api_name = api_name
    preset.save()
    return create_response_success()


# 删除装备预设
@require_POST
def preset_slot_delete(request):
    api_preset_id = int(request.POST.get("api_preset_id"))
    PresetService.del_preset_slot_by_id(api_preset_id)
    return create_response_success()
