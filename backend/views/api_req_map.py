from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from ..services.AdmiralService import AdmiralService
from ..services.MapService import MapService
from ..services.DeckService import DeckService
from ..bl.MapPointBL import MapPointBL
from .common import create_response, create_response_success


# 进入地图
@require_POST
def start(request):
    maparea_id = int(request.POST.get("api_maparea_id"))
    mapinfo_no = int(request.POST.get("api_mapinfo_no"))
    deck_id = int(request.POST.get("api_deck_id"))
    serial_cid = int(request.POST.get("api_serial_cid"))
    map_id = str(maparea_id) + str(mapinfo_no)

    current_point = 0

    deck = DeckService.get_deck_port_by_id(deck_id)
    map_point_info = MapService.get_map_point_info_by_id(maparea_id, mapinfo_no, current_point)
    next_map_point = MapPointBL.get_next_map_point(map_point_info, deck.api_ship)
    next_map_point_info = MapService.get_map_point_info_by_id(maparea_id, mapinfo_no, next_map_point)
    # 写入当前出击信息，供后续API调用
    MapService.set_current_battle_info(maparea_id, mapinfo_no, next_map_point, deck_id)
    api_data = {
        "api_cell_data": MapService.get_map_point_info(maparea_id, mapinfo_no),
        "api_rashin_flg": map_point_info.rashin_flg,  # 是否要转罗盘
        "api_rashin_id": map_point_info.rashin_id,  # 罗盘旋转的角度或方向ID？
        "api_maparea_id": maparea_id,
        "api_mapinfo_no": mapinfo_no,
        "api_no": next_map_point,  # 下一个点位编号
        "api_color_no": next_map_point_info.color_no,  # 下一个点位颜色编号
        "api_event_id": next_map_point_info.event_id,  # 下一个点位事件编号
        "api_event_kind": next_map_point_info.event_kind,  # 下一个点位事件类型
        "api_next": 1 if next_map_point_info.next_points else 0,  # 是否存在再下一个点 0：终点 1: 继续前进
        "api_bosscell_no": MapService.get_bosscell_no(maparea_id, mapinfo_no).point_no,  # boss点位编号
        "api_bosscomp": MapService.get_map_info_by_id(
            map_id
        ).api_cleared,  # 是否通关boss， 0: 未通关 / 血条未空 1: 已通关 / 已击破
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
    maparea_id = current_battle_info.maparea_id
    mapinfo_no = current_battle_info.mapinfo_no
    map_id = str(current_battle_info.maparea_id) + str(current_battle_info.mapinfo_no)
    deck = DeckService.get_deck_port_by_id(current_battle_info.deck_id)

    map_point_info = MapService.get_map_point_info_by_id(maparea_id, mapinfo_no, current_battle_info.current_point)
    next_map_point = MapPointBL.get_next_map_point(map_point_info, deck.api_ship)
    next_map_point_info = MapService.get_map_point_info_by_id(maparea_id, mapinfo_no, next_map_point)
    api_data = {
        "api_rashin_flg": map_point_info.rashin_flg,
        "api_rashin_id": map_point_info.rashin_id,
        "api_maparea_id": maparea_id,
        "api_mapinfo_no": mapinfo_no,
        "api_no": next_map_point,  # 下一个点位编号
        "api_color_no": next_map_point_info.color_no,  # 下一个点位颜色编号
        "api_event_id": next_map_point_info.event_id,  # 下一个点位事件编号
        "api_event_kind": next_map_point_info.event_kind,  # 下一个点位事件类型
        "api_next": 1 if next_map_point_info.next_points else 0,  # 是否存在再下一个点 0：终点 1: 继续前进
        "api_bosscell_no": MapService.get_bosscell_no(maparea_id, mapinfo_no).point_no,
        "api_bosscomp": MapService.get_map_info_by_id(map_id).api_cleared,
        "api_comment_kind": 0,
        "api_production_kind": 0,  # TODO “演出效果”。这个字段用来决定舰队到达该点时播放什么动画。例如：是播放普通的平移、遭遇战的警告红光、航空侦察
        "api_airsearch": {"api_plane_type": 0, "api_result": 0},
        "api_e_deck_info": [{"api_kind": 0, "api_ship_ids": [1505, 1501, 1501]}],
        "api_limit_state": 0,  # TODO 标记当前地点的锁船状态、史实舰加成限制，或某些有特殊出击条件（如联合舰队限高、禁止特定舰种进入）的状态。
        "api_ration_flag": 0,  # TODO 标记本场战斗中是否消耗并触发了“战斗粮食”（便当）
    }
    return create_response(api_data)
