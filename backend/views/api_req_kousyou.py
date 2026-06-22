from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from ..services.AdmiralService import AdmiralService
from ..services.MaterialService import MaterialService
from ..services.ShipService import ShipService
from ..services.MstService import MstService
from ..services.NdockService import NdockService
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
