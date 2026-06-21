from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from ..services.AdmiralService import AdmiralService
from ..services.MaterialService import MaterialService
from ..services.ShipService import ShipService
from ..services.MstService import MstService
from ..services.NdockService import NdockService
from .common import create_response, create_response_success
from ..utils import gameUtils


# 燃料弹药补给
@require_POST
def start(request):
    api_highspeed = int(request.POST.get("api_highspeed"))
    api_ndock_id = int(request.POST.get("api_ndock_id"))
    api_ship_id = int(request.POST.get("api_ship_id"))
    # 获取入渠舰娘
    ship = ShipService.get_ship_by_id(api_ship_id)
    # 获取入渠槽位
    ndock = NdockService.get_ndock_by_id(api_ndock_id)
    # 更新资源状态
    material = MaterialService.get_material()

    material.fuel -= ship.api_ndock_item[0]
    material.steel -= ship.api_ndock_item[1]
    material.save()
    # TODO 更新入渠资源状态
    ndock.api_item1 = ship.api_ndock_item[0]  # 燃料
    ndock.api_item2 = ship.api_ndock_item[1]  # 钢材
    # 计算入渠完成时间
    if api_highspeed == 1:
        # 高速修复, 直接更新舰娘状态
        gameUtils.fix_ship_status(ship)
    else:
        ndock.api_ship_id = api_ship_id
        ndock.api_state = 1
        ndock.api_complete_time = 0
        ndock.api_complete_time_str = "0"

    return create_response_success()
