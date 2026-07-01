from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from ..services.AdmiralService import AdmiralService
from ..services.MapService import MapService
from ..services.DeckService import DeckService
from .common import create_response, create_response_success


# 进入地图
@require_POST
def start(request):
    api_maparea_id = int(request.POST.get("api_maparea_id"))
    api_mapinfo_no = int(request.POST.get("api_mapinfo_no"))
    api_deck_id = int(request.POST.get("api_deck_id"))
    api_serial_cid = int(request.POST.get("api_serial_cid"))
    map_id = request.POST.get("api_maparea_id") + request.POST.get("api_mapinfo_no")

    deck = DeckService.get_deck_port_by_id(api_deck_id)
    next_map_point = MapService.get_next_map_point(map_id, "0", deck.api_ship)
    # 写入当前出击信息，供后续API调用
    MapService.set_current_battle_info(api_maparea_id, next_map_point, api_deck_id)

    api_data = {
        "api_cell_data": [
            {"api_id": 3001, "api_no": 0, "api_color_no": 0, "api_passed": 0},
            {"api_id": 3002, "api_no": 1, "api_color_no": 4, "api_passed": 1},
            {"api_id": 3003, "api_no": 2, "api_color_no": 4, "api_passed": 1},
            {"api_id": 3004, "api_no": 3, "api_color_no": 5, "api_passed": 1},
        ],  # 地图各个点位信息
        "api_rashin_flg": MapService.need_rashin(map_id, "0"),  # 是否要转罗盘
        "api_rashin_id": 1,  # 罗盘旋转的角度或方向ID？
        "api_maparea_id": api_maparea_id,
        "api_mapinfo_no": api_mapinfo_no,
        "api_no": next_map_point,  # 下一个点位编号
        "api_color_no": 4,
        "api_event_id": 4,
        "api_event_kind": 1,
        "api_next": 1,
        "api_bosscell_no": 3,  # boss点位编号
        "api_bosscomp": 1,  # 是否通关boss， 0: 未通关 / 血条未空 1: 已通关 / 已击破
        "api_airsearch": {"api_plane_type": 0, "api_result": 0},
        "api_e_deck_info": [{"api_kind": 0, "api_ship_ids": [1503]}],
        "api_limit_state": 0,
        "api_from_no": 0,
    }
    return create_response(api_data)


# 地图轮盘
@require_POST
def next(request):
    api_recovery_type = int(request.POST.get("api_recovery_type"))

    # 获取当前出击信息
    current_battle_info = MapService.get_current_battle_info()
    map_id = str(current_battle_info.api_maparea_id) + str(current_battle_info.api_mapinfo_no)
    deck = DeckService.get_deck_port_by_id(current_battle_info.api_deck_id)

    # TODO 建立地图信息数据库
    api_data = {
        "api_rashin_flg": MapService.need_rashin(map_id, current_battle_info.api_mapinfo_no),
        "api_rashin_id": 1,
        "api_maparea_id": current_battle_info.api_maparea_id,
        "api_mapinfo_no": current_battle_info.api_mapinfo_no,
        "api_no": MapService.get_next_map_point(map_id, current_battle_info.api_mapinfo_no, deck.api_ship),
        "api_color_no": 5,
        "api_event_id": 5,
        "api_event_kind": 1,
        "api_next": 0,
        "api_bosscell_no": 3,
        "api_bosscomp": 1,
        "api_comment_kind": 0,
        "api_production_kind": 0,
        "api_airsearch": {"api_plane_type": 0, "api_result": 0},
        "api_e_deck_info": [{"api_kind": 0, "api_ship_ids": [1505, 1501, 1501]}],
        "api_limit_state": 0,
        "api_ration_flag": 0,
    }
    return create_response(api_data)
