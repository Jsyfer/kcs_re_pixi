from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from django.views.decorators.http import require_POST
from ..services.AdmiralService import AdmiralService
from ..services.MaterialService import MaterialService
from ..services.ShipService import ShipService
from ..services.MstService import MstService
from ..services.NdockService import NdockService
from ..services.KdockService import KdockService
from ..services.SlotItemService import SlotItemService
from .common import create_response, create_response_success
from ..utils.Utils import Utils
from ..utils.GameUtils import GameUtils
from datetime import datetime


# 舰娘解体
@require_POST
def destroyship(request):
    api_ship_id_list = request.POST.get("api_ship_id").split(",")
    api_slot_dest_flag = int(request.POST.get("api_slot_dest_flag"))
    # 获取当前所持资源
    material = MaterialService.get_material()
    # 处理每艘待解体的舰娘
    for ship_id_str in api_ship_id_list:
        # 获取舰娘
        ship_id = int(ship_id_str)
        ship = ShipService.get_ship_by_id(ship_id)
        mst_ship = MstService.get_mst_ship_by_id(ship.api_ship_id)

        # 获取装备
        for item_id in ship.api_slot or []:
            if item_id != -1 and item_id != 0:
                # 获取装备
                item = SlotItemService.get_slot_item_by_id(item_id)
                mst_item = MstService.get_mst_slotitem_by_id(item.api_slotitem_id)
                # 是否同时废弃装备
                if api_slot_dest_flag == 1:
                    # 将装备废弃获得的资源加入库存
                    material.fuel += mst_item.api_broken[0]  # type: ignore
                    material.bull += mst_item.api_broken[1]  # type: ignore
                    material.steel += mst_item.api_broken[2]  # type: ignore
                    material.aluminium += mst_item.api_broken[3]  # type: ignore
                    # 删除装备
                    SlotItemService.del_slot_item_by_id(item_id)
                else:
                    # 将装备返回仓库
                    item.api_used_ship = -1
                    item.save()
        # 检查是否有ex装备
        if ship.api_slot_ex != -1 and ship.api_slot_ex != 0:
            # 获取ex装备
            item_ex = SlotItemService.get_slot_item_by_id(ship.api_slot_ex)
            mst_item_ex = MstService.get_mst_slotitem_by_id(item_ex.api_slotitem_id)
            # 是否同时废弃装备
            if api_slot_dest_flag == 1:
                # 将装备废弃获得的资源加入库存
                material.fuel += mst_item_ex.api_broken[0]  # type: ignore
                material.bull += mst_item_ex.api_broken[1]  # type: ignore
                material.steel += mst_item_ex.api_broken[2]  # type: ignore
                material.aluminium += mst_item_ex.api_broken[3]  # type: ignore
                # 删除装备
                SlotItemService.del_slot_item_by_id(item_id)
            else:
                # 将装备返回仓库
                item_ex.api_used_ship = -1
                item_ex.save()
        # 将解体舰娘获得的资源加入库存
        material.fuel += mst_ship.api_broken[0]  # type: ignore
        material.bull += mst_ship.api_broken[1]  # type: ignore
        material.steel += mst_ship.api_broken[2]  # type: ignore
        material.aluminium += mst_ship.api_broken[3]  # type: ignore
        # 删除舰娘
        ShipService.del_ship_by_id(ship_id)
    material.save()

    api_data = {"api_material": [material.fuel, material.bull, material.steel, material.aluminium]}
    return create_response(api_data)


# 废弃装备
@require_POST
def destroyitem2(request):
    api_item_id_list = request.POST.get("api_slotitem_ids").split(",")
    # 获取当前所持资源
    material = MaterialService.get_material()
    fuel_gained = 0
    bull_gained = 0
    steel_gained = 0
    aluminium_gained = 0
    for item_id_str in api_item_id_list:
        item_id = int(item_id_str)
        # 获取装备
        item = SlotItemService.get_slot_item_by_id(item_id)
        mst_item = MstService.get_mst_slotitem_by_id(item.api_slotitem_id)
        fuel_gained += mst_item.api_broken[0]  # type: ignore
        bull_gained += mst_item.api_broken[1]  # type: ignore
        steel_gained += mst_item.api_broken[2]  # type: ignore
        aluminium_gained += mst_item.api_broken[3]  # type: ignore
        # 删除装备
        SlotItemService.del_slot_item_by_id(item_id)

    # 将装备废弃获得的资源加入库存
    material.fuel += fuel_gained
    material.bull += bull_gained
    material.steel += steel_gained
    material.aluminium += aluminium_gained
    material.save()

    api_data = {"api_get_material": [fuel_gained, bull_gained, steel_gained, aluminium_gained]}
    return create_response(api_data)


# 获取舰娘
@require_POST
def getship(request):
    api_kdock_id = int(request.POST.get("api_kdock_id"))
    # 获取建造槽位
    kdock = KdockService.get_kdock_by_id(api_kdock_id)
    # 获取建造舰娘编号
    mst_ship_id = kdock.api_created_ship_id
    mst_ship = MstService.get_mst_ship_by_id(mst_ship_id)

    # 创建新舰娘
    ship_dict = {
        "api_backs": mst_ship.api_backs,  # 背景稀有度
        "api_bull": mst_ship.api_bull_max,
        "api_cond": 40,
        "api_exp": [0, 100, 0],
        "api_fuel": mst_ship.api_fuel_max,
        "api_kaihi": [mst_ship.min_kaihi, mst_ship.max_kaihi],
        "api_karyoku": mst_ship.api_houg,
        "api_kyouka": [0, 0, 0, 0, 0, 0, 0],
        "api_leng": mst_ship.api_leng,
        "api_locked": 0,
        "api_locked_equip": 0,
        "api_lucky": mst_ship.api_luck,
        "api_lv": 1,
        "api_maxhp": mst_ship.api_taik[0],  # type: ignore
        "api_ndock_item": [0, 0],
        "api_ndock_time": 0,
        "api_nowhp": mst_ship.api_taik[0],  # type: ignore
        "api_onslot": mst_ship.api_maxeq,
        "api_raisou": mst_ship.api_raig,
        "api_sakuteki": [mst_ship.min_sakuteki, mst_ship.max_sakuteki],
        "api_ship_id": mst_ship_id,
        "api_slot": [-1, -1, -1, -1, -1],
        "api_slot_ex": 0,
        "api_slotnum": mst_ship.api_slot_num,
        "api_soku": mst_ship.api_soku,
        "api_sortno": mst_ship.api_sortno,
        "api_soukou": mst_ship.api_souk,
        "api_srate": 0,  # 近代化改修进度0～4
        "api_taiku": mst_ship.api_tyku,
        "api_taisen": [mst_ship.min_taisen, mst_ship.max_taisen],
    }
    ship = ShipService.create_ship(ship_dict)

    # 创建舰娘初始装备
    api_slot = []
    api_slotitem = []
    if mst_ship.init_item:
        for mst_item_id in mst_ship.init_item:  # type: ignore
            item_id = SlotItemService.create_slot_item_by_id(mst_item_id)
            api_slot.append(item_id)
            api_slotitem.append({"api_id": item_id, "api_slotitem_id": mst_item_id})

    # 将装备赋予舰娘
    for i, item_id in enumerate(api_slot):
        ship.api_slot[i] = item_id
    GameUtils.update_ship_status_with_slot_items(ship)
    ship.save()

    # 恢复建造槽位为未使用
    kdock.api_state = 0
    kdock.api_created_ship_id = -1
    kdock.api_complete_time = 0
    kdock.api_complete_time_str = "0"
    kdock.api_item1 = 0
    kdock.api_item2 = 0
    kdock.api_item3 = 0
    kdock.api_item4 = 0
    kdock.api_item5 = 1
    kdock.save()
    api_data = {
        "api_id": ship.api_id,
        "api_kdock": KdockService.get_kdock(),
        "api_ship": model_to_dict(ship),
        "api_ship_id": mst_ship_id,
        "api_slotitem": api_slotitem,
    }
    return create_response(api_data)


# 通常建造
@require_POST
def createship(request):
    api_kdock_id = int(request.POST.get("api_kdock_id"))
    api_large_flag = int(request.POST.get("api_large_flag"))
    fuel = int(request.POST.get("api_item1"))
    bull = int(request.POST.get("api_item2"))
    steel = int(request.POST.get("api_item3"))
    aluminium = int(request.POST.get("api_item4"))
    development = int(request.POST.get("api_item5"))
    construction = int(request.POST.get("api_highspeed"))

    # 获取建造槽位
    kdock = KdockService.get_kdock_by_id(api_kdock_id)
    # TODO 根据资源判断建造舰娘对象
    mst_ship_id = 931
    mst_ship = MstService.get_mst_ship_by_id(mst_ship_id)

    # 若未使用高速建造
    if construction == 0:
        complete_time = Utils.get_current_timestamp() + (mst_ship.api_buildtime or 0) * 60 * 1000
        kdock.api_complete_time = complete_time
        kdock.api_complete_time_str = Utils.convert_readable_time(complete_time)

    # 更新建造槽位
    kdock.api_state = MstService.get_mst_stype_by_id(mst_ship.api_stype).api_kcnt
    kdock.api_created_ship_id = mst_ship_id
    kdock.api_item1 = fuel
    kdock.api_item2 = bull
    kdock.api_item3 = steel
    kdock.api_item4 = aluminium
    kdock.api_item5 = development
    kdock.save()

    # 消耗库存资源
    material = MaterialService.get_material()
    material.fuel -= fuel
    material.bull -= bull
    material.steel -= steel
    material.aluminium -= aluminium
    material.development -= development
    material.construction -= construction
    material.save()

    return create_response_success()
