from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.forms.models import model_to_dict
from ..services.ShipService import ShipService
from ..services.SlotItemService import SlotItemService
from ..services.MstService import MstService
from ..services.PresetService import PresetService
from ..services.DeckService import DeckService
from .common import create_response, create_response_success
from ..utils.GameUtils import GameUtils


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
    GameUtils.update_slotitem_used_by_ship(ship.api_slot, -1)
    # 更新舰娘api_slot
    (ship.api_slot or [])[:] = [-1] * len(ship.api_slot or [])
    GameUtils.update_ship_status_with_slot_items(ship)
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
    GameUtils.update_slotitem_used_by_ship([(ship.api_slot or [])[api_slot_idx]], -1)
    # 更新舰娘api_slot对应位置装备
    (ship.api_slot or [])[api_slot_idx] = api_item_id
    # 设置新装备使用者为当前舰娘
    GameUtils.update_slotitem_used_by_ship([api_item_id], api_id)
    # 更新舰娘状态
    GameUtils.update_ship_status_with_slot_items(ship)
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
    GameUtils.update_slotitem_used_by_ship([ship.api_slot_ex], -1)
    # 更新舰娘exslot装备
    ship.api_slot_ex = api_item_id
    # 设置新装备使用者为当前舰娘
    GameUtils.update_slotitem_used_by_ship([api_item_id], api_id)
    # 更新舰娘状态
    GameUtils.update_ship_status_with_slot_items(ship)
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
    GameUtils.update_slotitem_used_by_ship([unset_item_id], api_set_ship)
    # 更新被替换掉装备使用者为无
    GameUtils.update_slotitem_used_by_ship([set_item_id], -1)
    # 更新舰娘api_slot对应位置装备
    if api_set_slot_kind == 1:
        set_ship.api_slot_ex = unset_item_id
    else:
        (set_ship.api_slot or [])[api_set_idx] = unset_item_id
    GameUtils.update_ship_status_with_slot_items(set_ship)
    set_ship.save()
    # 从该装备原来所属舰娘卸载装备
    if api_unset_slot_kind == 1:
        unset_ship.api_slot_ex = -1
    else:
        (unset_ship.api_slot or [])[api_unset_idx] = -1
    GameUtils.update_ship_status_with_slot_items(unset_ship)
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
                "api_slot_list": SlotItemService.get_unset_slots()["api_slottype" + str(api_type)],  # type: ignore
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
            GameUtils.update_slotitem_used_by_ship([ship.api_slot_ex], -1)
            ship.api_slot_ex = unset_slot_item.api_id
            unset_slot_item.save()
    # 设置旧装备为未使用
    GameUtils.update_slotitem_used_by_ship(ship.api_slot, -1)
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
    GameUtils.update_ship_status_with_slot_items(ship)
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


# 为舰娘增加ex装备槽
@require_POST
def open_exslot(request):
    api_id = int(request.POST.get("api_id"))
    ship = ShipService.get_ship_by_id(api_id)
    ship.api_slot_ex = -1
    ship.save()
    return create_response_success()


# 近代化改修
@require_POST
def powerup(request):
    api_id = int(request.POST.get("api_id"))
    api_id_items = request.POST.get("api_id_items").split(",")
    api_slot_dest_flag = int(request.POST.get("api_slot_dest_flag"))
    api_limited_feed_type = int(request.POST.get("api_limited_feed_type"))

    kyoka_hp = 0
    kyoka_karyoku = 0
    kyoka_raisou = 0
    kyoka_taiku = 0
    kyoka_soukou = 0
    kyoka_lucky = 0

    api_unset_items = []

    ship = ShipService.get_ship_by_id(api_id)
    for ship_id_str in api_id_items:
        ship_id = int(ship_id_str)
        ship_to_consume = ShipService.get_ship_by_id(ship_id)
        mst_ship_to_consume = MstService.get_mst_ship_by_id(ship_to_consume.api_ship_id)

        # 处理用于强化的舰娘的装备
        for item_id in ship_to_consume.api_slot or []:
            if item_id != -1 and item_id != 0:
                # 获取装备
                item = SlotItemService.get_slot_item_by_id(item_id)
                mst_item = MstService.get_mst_slotitem_by_id(item.api_slotitem_id)
                # 是否同时废弃装备
                if api_slot_dest_flag == 1:
                    # 删除装备
                    SlotItemService.del_slot_item_by_id(item_id)
                else:
                    # 将装备返回仓库
                    item.api_used_ship = -1
                    item.save()
                    api_type = mst_item.api_type[2]  # type: ignore
                    if any(d.get("api_type3No") == api_type for d in api_unset_items):
                        matched_dict = next((d for d in api_unset_items if d.get("api_type3No") == api_type), None)
                        if matched_dict:
                            matched_dict["api_slot_list"].append(item_id)
                    else:
                        api_unset_items.append(
                            {
                                "api_slot_list": SlotItemService.get_unset_slots()["api_slottype" + str(api_type)],
                                "api_type3No": api_type,
                            }
                        )
        # 检查用于强化的舰娘是否有ex装备
        if ship.api_slot_ex != -1 and ship.api_slot_ex != 0:
            # 获取ex装备
            item_ex = SlotItemService.get_slot_item_by_id(ship.api_slot_ex)
            mst_item_ex = MstService.get_mst_slotitem_by_id(item_ex.api_slotitem_id)
            # 是否同时废弃装备
            if api_slot_dest_flag == 1:
                # 删除装备
                SlotItemService.del_slot_item_by_id(item_id)
            else:
                # 将装备返回仓库
                item_ex.api_used_ship = -1
                item_ex.save()
                api_type = mst_item_ex.api_type[2]  # type: ignore
                if any(d.get("api_type3No") == api_type for d in api_unset_items):
                    matched_dict = next((d for d in api_unset_items if d.get("api_type3No") == api_type), None)
                    if matched_dict:
                        matched_dict["api_slot_list"].append(item_id)
                else:
                    api_unset_items.append(
                        {
                            "api_slot_list": SlotItemService.get_unset_slots()["api_slottype" + str(api_type)],
                            "api_type3No": api_type,
                        }
                    )
        # TODO 若消耗舰娘为海防舰则增加HP和运
        # TODO 若消耗舰娘为まるゆ则增加运
        kyoka_karyoku += mst_ship_to_consume.api_powup[0]  # type: ignore
        kyoka_raisou += mst_ship_to_consume.api_powup[1]  # type: ignore
        kyoka_taiku += mst_ship_to_consume.api_powup[2]  # type: ignore
        kyoka_soukou += mst_ship_to_consume.api_powup[3]  # type: ignore

        # 消耗舰娘
        ShipService.del_ship_by_id(ship_id)

    # TODO 若满足条件则强化数值获得额外提升
    if kyoka_hp >= 4:
        kyoka_hp += 1
    if kyoka_karyoku >= 4:
        kyoka_karyoku += 1
    if kyoka_raisou >= 4:
        kyoka_raisou += 1
    if kyoka_taiku >= 4:
        kyoka_taiku += 1
    if kyoka_soukou >= 4:
        kyoka_soukou += 1
    if kyoka_lucky >= 4:
        kyoka_lucky += 1

    ship.api_maxhp += kyoka_hp  # type: ignore
    ship.api_karyoku = [ship.api_karyoku[0] + kyoka_karyoku, ship.api_karyoku[1]]  # type: ignore
    ship.api_raisou = [ship.api_raisou[0] + kyoka_raisou, ship.api_raisou[1]]  # type: ignore
    ship.api_taiku = [ship.api_taiku[0] + kyoka_taiku, ship.api_taiku[1]]  # type: ignore
    ship.api_soukou = [ship.api_soukou[0] + kyoka_soukou, ship.api_soukou[1]]  # type: ignore
    ship.api_lucky = [ship.api_lucky[0] + kyoka_lucky, ship.api_lucky[1]]  # type: ignore

    ship.save()
    api_data = {
        "api_deck": DeckService.get_deck_port(),
        "api_powerup_flag": 1,
        "api_ship": model_to_dict(ship),
        "api_unset_list": api_unset_items,
    }
    return create_response(api_data)


# 改造
@require_POST
def remodeling(request):
    api_id = int(request.POST.get("api_id"))

    ship = ShipService.get_ship_by_id(api_id)
    mst_ship_current = MstService.get_mst_ship_by_id(ship.api_ship_id)

    mst_after_ship = MstService.get_mst_ship_by_id(int(mst_ship_current.api_aftershipid))  # type: ignore
    # 移除旧装备
    for item_id in ship.api_slot:
        if item_id != -1:
            item = SlotItemService.get_slot_item_by_id(item_id)
            item.api_used_ship = -1
            item.save()
    if ship.api_slot_ex != -1:
        item_ex = SlotItemService.get_slot_item_by_id(ship.api_slot_ex)
        item_ex.api_used_ship = -1
        item_ex.save()
    # 创建新装备
    after_ship_items = []
    if mst_after_ship.init_item:
        for item_id in mst_after_ship.init_item:  # type: ignore
            new_item_id = SlotItemService.create_slot_item_by_id(item_id)
            after_ship_items.append(new_item_id)

    # 进行改造
    ship.api_ship_id = mst_after_ship.api_id
    ship.api_sortno = mst_after_ship.api_sortno
    ship.api_nowhp = mst_after_ship.api_taik[1]  # type: ignore
    ship.api_maxhp = mst_after_ship.api_taik[1]  # type: ignore
    ship.api_slot = after_ship_items
    ship.api_onslot = mst_after_ship.api_maxeq
    if ship.api_slot_ex != 0:
        ship.api_slot_ex = -1
    ship.api_backs = mst_after_ship.api_backs
    ship.api_fuel = mst_after_ship.api_fuel_max
    ship.api_bull = mst_after_ship.api_bull_max
    ship.api_slotnum = mst_after_ship.api_slot_num
    ship.api_ndock_time = 0
    ship.api_ndock_item = [0, 0]  # type: ignore
    ship.api_cond = 40
    ship.api_locked_equip = 0
    GameUtils.update_ship_status_with_slot_items(ship)
    ship.save()
    # TODO 消耗各类改造资源

    return create_response_success()
