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
    mst_ship = MstService.get_mst_ship_by_id(ship.api_ship_id)

    # 获取新装备
    item = SlotItemService.get_slot_item_by_id(api_item_id)
    mst_item = MstService.get_mst_slotitem_by_id(item.api_slotitem_id)
    # 更新舰娘api_slot对应位置装备
    (ship.api_slot or [])[api_slot_idx] = api_item_id

    # 获取舰娘基础属性
    # 火力
    base_karyoku = mst_ship.api_houg[0] + ship.api_kyouka[0]  # type: ignore
    # 雷装
    base_raisou = mst_ship.api_raig[0] + ship.api_kyouka[1]  # type: ignore
    # 对空
    base_taiku = mst_ship.api_tyku[0] + ship.api_kyouka[2]  # type: ignore
    # 装甲
    base_soukou = mst_ship.api_souk[0] + ship.api_kyouka[3]  # type: ignore
    # 射程
    base_leng = ship.api_leng  # type: ignore
    # 速力
    base_soku = mst_ship.api_soku  # type: ignore
    # 索敌
    base_sakuteki = gameUtils.get_ship_base_sakuteki(ship.api_ship_id, ship.api_lv)
    # 回避
    base_kaihi = gameUtils.get_ship_base_kaihi(ship.api_ship_id, ship.api_lv)
    # 对潜
    base_taisen = gameUtils.get_ship_base_taisen(ship.api_ship_id, ship.api_lv)
    # TODO 计算装备属性加成

    # 更新舰娘属性
    ship.api_karyoku = [base_karyoku, ship.api_karyoku[1]]  # type: ignore
    ship.api_raisou = [base_raisou, ship.api_raisou[1]]  # type: ignore
    ship.api_taiku = [base_taiku, ship.api_taiku[1]]  # type: ignore
    ship.api_soukou = [base_soukou, ship.api_soukou[1]]  # type: ignore
    ship.api_taisen = [base_taisen, ship.api_taisen[1]]  # type: ignore
    ship.api_kaihi = [base_kaihi, ship.api_kaihi[1]]  # type: ignore
    ship.api_leng = base_leng  # type: ignore
    ship.api_soku = base_soku  # type: ignore
    ship.api_sakuteki = [base_sakuteki, ship.api_sakuteki[1]]  # type: ignore

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
