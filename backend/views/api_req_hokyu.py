from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from ..services.AdmiralService import AdmiralService
from ..services.MaterialService import MaterialService
from ..services.ShipService import ShipService
from ..services.MstService import MstService
from .common import create_response


@require_POST
def charge(request):
    request_data = request.POST
    api_kind = request_data.get("api_kind")
    ship_id_list = request_data.get("api_id_items").split(",")
    api_onslot = request_data.get("api_onslot")

    result_ship_list = []

    # 当前资源保有情况
    fuel = MaterialService.get_material_by_id(1)
    bull = MaterialService.get_material_by_id(2)
    steel = MaterialService.get_material_by_id(3)
    aluminium = MaterialService.get_material_by_id(4)
    fuel_consumption = 0
    bull_consumption = 0
    aluminium_consumption = 0
    for ship_id in ship_id_list:
        ship = ShipService.get_ship_by_id(int(ship_id))
        mst_ship = MstService.get_mst_ship_by_id(ship.api_ship_id)
        if api_kind == "0":
            # 舰载机补充
            aluminium_consumption += (
                sum(mst_ship.api_maxeq or []) - sum(ship.api_onslot or [])
            ) * 5
            # 更新舰船状态
            ship.api_onslot = mst_ship.api_maxeq
        elif api_kind == "3":
            # 全補給
            # 燃料与弹药消耗
            current_fuel_cons = (mst_ship.api_fuel_max or 0) - (ship.api_fuel or 0)
            current_bull_cons = (mst_ship.api_bull_max or 0) - (ship.api_bull or 0)
            # 婚舰燃料与弹药：出击补给时，消耗量减少 15%（计算后向下取整）
            if (ship.api_lv or 0) > 99:
                current_fuel_cons = int(current_fuel_cons * 0.85)
                current_bull_cons = int(current_bull_cons * 0.85)
            fuel_consumption += current_fuel_cons
            bull_consumption += current_bull_cons
            # 舰载机补充
            aluminium_consumption += (
                sum(mst_ship.api_maxeq or []) - sum(ship.api_onslot or [])
            ) * 5
            # 更新舰船状态
            ship.api_fuel = mst_ship.api_fuel_max
            ship.api_bull = mst_ship.api_bull_max
            ship.api_onslot = mst_ship.api_maxeq

        ship.save()
        result_ship_list.append(
            {
                "api_bull": ship.api_bull,
                "api_fuel": ship.api_fuel,
                "api_id": ship.api_id,
                "api_onslot": ship.api_onslot,
            }
        )
    # 更新各资源消耗
    if api_kind == "3":
        fuel.api_value = fuel.api_value - fuel_consumption
        fuel.save()
        bull.api_value = bull.api_value - bull_consumption
        bull.save()
    aluminium.api_value = aluminium.api_value - aluminium_consumption
    aluminium.save()

    api_data = {
        "api_material": [
            fuel.api_value,
            bull.api_value,
            steel.api_value,
            aluminium.api_value,
        ],
        "api_ship": result_ship_list,
        "api_use_bou": aluminium_consumption,
    }

    return create_response(api_data)
