from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from ..services.AdmiralService import AdmiralService
from ..services.MaterialService import MaterialService
from ..services.ShipService import ShipService
from ..services.MstService import MstService
from ..services.NdockService import NdockService
from .common import create_response, create_response_success
from ..utils.Utils import Utils
from ..utils.GameUtils import GameUtils
from datetime import datetime


# 燃料弹药补给
@require_POST
def start(request):
    api_highspeed = int(request.POST.get("api_highspeed"))
    api_ndock_id = int(request.POST.get("api_ndock_id"))
    api_ship_id = int(request.POST.get("api_ship_id"))
    # 获取入渠舰娘
    ship = ShipService.get_ship_by_id(api_ship_id)

    # 更新资源状态
    material = MaterialService.get_material()
    material.fuel -= ship.api_ndock_item[0]
    material.steel -= ship.api_ndock_item[1]

    # 计算入渠完成时间
    if api_highspeed == 1:
        # 高速修复, 直接更新舰娘状态
        GameUtils.fix_ship_status(ship)
        material.repair -= 1
    else:
        # 获取入渠槽位
        ndock = NdockService.get_ndock_by_id(api_ndock_id)
        complete_timestamp = GameUtils.calculate_repair_complete_time(ship)
        ndock.api_ship_id = api_ship_id
        ndock.api_state = 1
        ndock.api_complete_time = complete_timestamp
        ndock.api_complete_time_str = Utils.convert_readable_time(complete_timestamp)
        # 更新入渠资源状态
        ndock.api_item1 = ship.api_ndock_item[0]  # 燃料
        ndock.api_item2 = ship.api_ndock_item[1]  # 钢材
        ndock.save()
    material.save()
    return create_response_success()


# 快速修复
@require_POST
def speedchange(request):
    api_ndock_id = int(request.POST.get("api_ndock_id"))
    # 获取入渠槽位
    ndock = NdockService.get_ndock_by_id(api_ndock_id)
    # 获取入渠舰娘
    ship = ShipService.get_ship_by_id(ndock.api_ship_id)

    # 高速修复, 直接更新舰娘状态
    GameUtils.fix_ship_status(ship)

    # 更新资源状态
    material = MaterialService.get_material()
    material.repair -= 1

    ndock.api_ship_id = 0
    ndock.api_state = 0
    ndock.api_complete_time = 0
    ndock.api_complete_time_str = "0"
    # 更新入渠资源状态
    ndock.api_item1 = 0  # 燃料
    ndock.api_item2 = 0  # 钢材
    ndock.save()
    material.save()
    return create_response_success()
