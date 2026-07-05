from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from ..services.MstService import MstService
from ..services.AdmiralService import AdmiralService
from ..services.MapService import MapService
from ..services.DeckService import DeckService
from ..bl.BattleBL import BattleBL
from ..bl.BattleResultBL import BattleResultBL
from ..bl.MapEnemyBL import MapEnemyBL
from .common import create_response, create_response_success


# 获取战斗信息
@require_POST
def battle(request):
    api_formation = int(request.POST.get("api_formation"))
    api_recovery_type = int(request.POST.get("api_recovery_type"))

    # 获取当前出击信息
    current_battle_info = MapService.get_current_battle_info()
    maparea_id = current_battle_info.maparea_id
    mapinfo_no = current_battle_info.mapinfo_no
    deck = DeckService.get_deck_port_by_id(current_battle_info.deck_id)
    f_ship_list = deck.api_ship
    enemy_info = MapService.get_map_enemy_by_id(current_battle_info.enemy_info_id)

    # 1. 索敵
    sakuteki_result = BattleBL.is_sakuteki_success(f_ship_list)
    # 2. (基地航空隊噴式強襲)
    # 3. (噴式強襲)
    # 4. (基地航空隊航空戦)
    # 5. (機動部隊(航空)友軍)
    # 6. 航空戦(制空権の決定を含む)
    # 7. (支援艦隊攻撃)
    # 8. 先制対潜攻撃
    # 9. 開幕雷撃
    # 10. 交戦形態の表示(交戦形態自体は戦闘開始時に決まっている模様)
    # 11. 砲撃戦→(砲撃戦2巡目)
    # 12. 雷撃戦→戦闘終了or夜戦突入判定
    # 13. (友軍艦隊攻撃)
    # 14. 夜戦

    f_deck_info = BattleBL.get_f_deck_info(f_ship_list)
    e_deck_info = BattleBL.get_e_deck_info(enemy_info.enemy)

    api_data = {
        "api_deck_id": current_battle_info.deck_id,
        "api_formation": [api_formation, enemy_info.formation, BattleBL.get_direction(f_ship_list)],
        "api_f_nowhps": f_deck_info["now_hp_info"],
        "api_f_maxhps": f_deck_info["max_hp_info"],
        "api_fParam": f_deck_info["base_param"],
        "api_ship_ke": enemy_info.enemy,
        "api_ship_lv": e_deck_info["ship_lv"],
        "api_e_nowhps": e_deck_info["now_hp_info"],
        "api_e_maxhps": e_deck_info["max_hp_info"],
        "api_eSlot": enemy_info.equip or e_deck_info["slot_item"],
        "api_eParam": e_deck_info["base_param"],
        "api_smoke_type": 0,
        "api_balloon_cell": 0,
        "api_atoll_cell": 0,
        "api_midnight_flag": 0,
        "api_search": [sakuteki_result, 5],
        "api_stage_flag": [1, 0, 0],
        "api_kouku": {
            "api_plane_from": [None, None],
            "api_stage1": {
                "api_f_count": 0,
                "api_f_lostcount": 0,
                "api_e_count": 0,
                "api_e_lostcount": 0,
                "api_disp_seiku": 1,
                "api_touch_plane": [-1, -1],
            },
            "api_stage2": None,
            "api_stage3": None,
        },
        "api_support_flag": 0,  # 支援舰队
        "api_support_info": None,
        "api_opening_taisen_flag": 0,  # 开幕对潜
        "api_opening_taisen": None,
        "api_opening_flag": 0,  # 开幕雷击
        "api_opening_atack": None,
        "api_hourai_flag": [1, 0, 0, 0],
        "api_hougeki1": {
            "api_at_eflag": [0],
            "api_at_list": [0],
            "api_at_type": [0],
            "api_df_list": [[0]],
            "api_si_list": [[4]],
            "api_cl_list": [[2]],
            "api_damage": [[30]],
        },
        "api_hougeki2": None,
        "api_hougeki3": None,
        "api_raigeki": None,
    }
    return create_response(api_data)


# 获取战斗信息
@require_POST
def battleresult(request):
    api_btime = int(request.POST.get("api_btime"))
    api_l_value = request.POST.get("api_l_value")  # 舰船血量信息
    api_l_value3 = request.POST.get("api_l_value3")

    admiral = AdmiralService.get_admiral_obj()

    # 获取当前出击信息
    current_battle_info = MapService.get_current_battle_info()
    maparea_id = current_battle_info.maparea_id
    mapinfo_no = current_battle_info.mapinfo_no
    deck = DeckService.get_deck_port_by_id(current_battle_info.deck_id)

    enemy_info = MapService.get_map_enemy_by_id(current_battle_info.enemy_info_id)
    map_point_info = MapService.get_map_point_info_by_id(maparea_id, mapinfo_no, current_battle_info.current_point)
    f_deck_info = BattleBL.get_f_deck_info(deck.api_ship)
    e_deck_info = BattleBL.get_e_deck_info(enemy_info.enemy)
    mst_mapinfo = MstService.get_mst_mapinfo_by_id(maparea_id, mapinfo_no)

    admiral_exp = BattleResultBL.cal_admiral_exp("S", mst_mapinfo, map_point_info)
    droped_ship = BattleResultBL.get_droped_ship(map_point_info)
    api_data = {
        "api_ship_id": enemy_info.enemy,
        "api_win_rank": "S",
        "api_get_exp": admiral_exp,
        "api_mvp": 1,
        "api_member_lv": admiral.api_level,
        "api_member_exp": admiral.api_experience,
        "api_get_base_exp": enemy_info.exp,
        "api_get_ship_exp": BattleResultBL.cal_ship_exp(deck.api_ship, enemy_info.exp, 1, "S"),
        "api_get_exp_lvup": BattleResultBL.get_ship_exp_info(deck.api_ship),
        "api_dests": 1,  # 击沉敌舰的总数量
        "api_destsf": 1,  # 是否击沉敌方旗舰
        "api_quest_name": mst_mapinfo.api_name,
        "api_quest_level": mst_mapinfo.api_level,
        "api_enemy_info": {"api_level": "", "api_rank": "", "api_deck_name": enemy_info.deck_name},
        "api_first_clear": 0 if map_point_info.passed == 1 else 1,
        "api_mapcell_incentive": 0,  # 地图格子额外奖励标志
        "api_get_flag": [0, 1 if droped_ship else 0, 0],  # 是否掉落物品，舰娘
        "api_get_ship": droped_ship,
        "api_get_eventflag": 0,  # 活动海域奖励标志
        "api_get_exmap_rate": 0,  # （EO 勋章图）血条扣减比，0 说明不是 EO 图或者血条没变化。
        "api_get_exmap_useitem_id": 0,
        "api_escape_flag": 0,  # 舰队退避机制标志
        "api_escape": None,
    }
    return create_response(api_data)
