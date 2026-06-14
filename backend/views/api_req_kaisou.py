from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from ..services.ShipService import ShipService
from ..services.SlotItemService import SlotItemService
from ..services.MstService import MstService
from .common import create_response, create_response_success


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
    mst_ship = MstService.get_mst_ship_by_id(ship.api_ship_id)
    # 获取旧装备
    old_mst_item = None
    if ship.api_slot[api_slot_idx] != -1:  # type: ignore
        old_item = SlotItemService.get_slot_item_by_id(ship.api_slot[api_slot_idx])  # type: ignore
        old_mst_item = MstService.get_mst_slotitem_by_id(old_item.api_slotitem_id)
    # 获取新装备
    item = SlotItemService.get_slot_item_by_id(api_item_id)
    mst_item = MstService.get_mst_slotitem_by_id(item.api_slotitem_id)
    # 更新舰娘api_slot对应位置装备
    (ship.api_slot or [])[api_slot_idx] = api_item_id
    # 根据装备属性，重新计算舰娘属性
    # TODO 装备属性加成
    # 火力
    new_karyoku = ship.api_karyoku[0] + mst_item.api_houg  # type: ignore
    # 雷装
    new_raisou = ship.api_raisou[0] + mst_item.api_raig  # type: ignore
    # 对空
    new_taiku = ship.api_taiku[0] + mst_item.api_tyku  # type: ignore
    # 装甲
    new_soukou = ship.api_soukou[0] + mst_item.api_souk  # type: ignore
    # 对潜
    new_taisen = ship.api_taisen[0] + mst_item.api_tais  # type: ignore
    # 回避
    new_kaihi = ship.api_kaihi[0] + mst_item.api_houk  # type: ignore
    # 射程
    new_leng = ship.api_leng + mst_item.api_leng  # type: ignore
    # 速力
    new_soku = ship.api_soku + mst_item.api_souk  # type: ignore
    # 索敌
    new_sakuteki = ship.api_sakuteki[0] + mst_item.api_saku  # type: ignore
    # 若旧装备存在，则减去旧装备属性
    if old_mst_item:
        new_karyoku -= old_mst_item.api_houg
        new_raisou -= old_mst_item.api_raig
        new_taiku -= old_mst_item.api_tyku
        new_soukou -= old_mst_item.api_souk
        new_taisen -= old_mst_item.api_tais
        new_kaihi -= old_mst_item.api_houk
        new_leng -= old_mst_item.api_leng  # type: ignore
        new_soku -= old_mst_item.api_soku  # type: ignore
        new_sakuteki -= old_mst_item.api_saku

    # 更新舰娘属性
    ship.api_karyoku = [new_karyoku, ship.api_karyoku[1]]  # type: ignore
    ship.api_raisou = [new_raisou, ship.api_raisou[1]]  # type: ignore
    ship.api_taiku = [new_taiku, ship.api_taiku[1]]  # type: ignore
    ship.api_soukou = [new_soukou, ship.api_soukou[1]]  # type: ignore
    ship.api_taisen = [new_taisen, ship.api_taisen[1]]  # type: ignore
    ship.api_kaihi = [new_kaihi, ship.api_kaihi[1]]  # type: ignore
    ship.api_leng = new_leng  # type: ignore
    ship.api_soku = new_soku  # type: ignore
    ship.api_sakuteki = [new_sakuteki, ship.api_sakuteki[1]]  # type: ignore

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
