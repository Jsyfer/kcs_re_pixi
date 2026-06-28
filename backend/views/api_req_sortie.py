from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from ..services.AdmiralService import AdmiralService
from .common import create_response, create_response_success


# 获取战斗信息
@require_POST
def battle(request):
    api_formation = int(request.POST.get("api_formation"))
    api_recovery_type = int(request.POST.get("api_recovery_type"))

    api_data = {
        "api_deck_id": 1,
        "api_formation": [1, 1, 3],
        "api_f_nowhps": [25, 16],
        "api_f_maxhps": [25, 16],
        "api_fParam": [[14, 24, 13, 10], [10, 24, 9, 7]],
        "api_ship_ke": [1503],
        "api_ship_lv": [1],
        "api_e_nowhps": [24],
        "api_e_maxhps": [24],
        "api_eSlot": [[1502, 1513, -1, -1, -1]],
        "api_eParam": [[6, 16, 6, 7]],
        "api_smoke_type": 0,
        "api_balloon_cell": 0,
        "api_atoll_cell": 0,
        "api_midnight_flag": 0,
        "api_search": [4, 5],
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
        "api_support_flag": 0,
        "api_support_info": None,
        "api_opening_taisen_flag": 0,
        "api_opening_taisen": None,
        "api_opening_flag": 0,
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
    api_l_value = request.POST.get("api_l_value")
    api_l_value3 = request.POST.get("api_l_value3")

    api_data = {
        "api_ship_id": [1503],
        "api_win_rank": "S",
        "api_get_exp": 10,
        "api_mvp": 1,
        "api_member_lv": 120,
        "api_member_exp": 56103357,
        "api_get_base_exp": 20,
        "api_get_ship_exp": [-1, 72, 24, -1, -1, -1, -1],
        "api_get_exp_lvup": [[0, 100], [180, 300]],
        "api_dests": 1,
        "api_destsf": 1,
        "api_quest_name": "鎮守府正面海域",
        "api_quest_level": 1,
        "api_enemy_info": {"api_level": "", "api_rank": "", "api_deck_name": "敵偵察艦"},
        "api_first_clear": 0,
        "api_mapcell_incentive": 0,
        "api_get_flag": [0, 1, 0],
        "api_get_ship": {
            "api_ship_id": 49,
            "api_ship_type": "駆逐艦",
            "api_ship_name": "霞",
            "api_ship_getmes": "霞よ。<br>ガンガンいくわよ。ついてらっしゃい。",
        },
        "api_get_eventflag": 0,
        "api_get_exmap_rate": 0,
        "api_get_exmap_useitem_id": 0,
        "api_escape_flag": 0,
        "api_escape": None,
    }
    return create_response(api_data)
