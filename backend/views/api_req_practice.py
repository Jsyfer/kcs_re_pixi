from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST

from ..services.AdmiralService import AdmiralService
from ..services.DeckService import DeckService
from ..services.FurnitureService import FurnitureService
from ..services.LogService import LogService
from ..services.MaterialService import MaterialService
from ..services.NdockService import NdockService
from ..services.ShipService import ShipService
from ..services.PracticeService import PracticeService
from .common import create_response
from django.conf import settings


# 切换演习后补
@require_POST
def change_matching_kind(request):
    api_selected_kind = int(request.POST.get("api_selected_kind"))
    api_data = {"api_update_flag": api_selected_kind}
    return create_response(api_data)


# 开始演习
# reference https://zh.kcwiki.cn/wiki/%E6%88%98%E6%96%97#.E6.88.98.E6.96.97.E6.B5.81.E7.A8.8B
@require_POST
def battle(request):
    api_deck_id = int(request.POST.get("api_deck_id"))
    api_formation_id = int(request.POST.get("api_formation_id"))
    api_enemy_id = int(request.POST.get("api_enemy_id"))
    # 获取我方编队信息
    deck_port = DeckService.get_deck_port_by_id(api_deck_id)
    f_ship_list = []
    api_fParam = []
    api_f_maxhps = []
    for ship_id in deck_port.api_ship:
        f_ship = ShipService.get_ship_by_id(ship_id)
        f_ship_list.append(f_ship)
        api_fParam.append([f_ship.api_karyoku, f_ship.api_raisou, f_ship.api_taiku, f_ship.api_soukou])
        api_f_maxhps.append(f_ship.api_maxhp)
    # 获取敌方编队信息

    # 阵形选择（进入战斗状态之前）
    # 根据阵型确定攻击力，命中，回避，对空补正，援护几率

    # 索敌
    # 判断索敌是否成功
    # 索敌成功时参加航空战
    # 如果索敌失败则不能参加航空战，此时如果对方制空值不为零，则自动失去制空权。

    # （基地航空队喷式强袭）

    # （喷式强袭）

    # （基地航空队航空战）

    # 航空战

    # 决定制空权

    # （支援舰队攻击）

    # 先制对潜攻击

    # 开幕雷击

    # 交战形态的表示

    # 炮击战

    # 第二轮炮击战

    # 雷击战

    # 追击选择

    # “战斗结束”或“夜战突入”

    # 夜战

    # 计算燃料弹药消耗

    api_data = {
        "api_atoll_cell": 0,
        "api_balloon_cell": 0,
        "api_deck_id": api_deck_id,
        "api_eParam": [
            [17, 0, 28, 28],
            [58, 56, 114, 52],
            [42, 98, 71, 54],
            [57, 53, 116, 53],
            [68, 87, 64, 54],
            [67, 89, 69, 54],
        ],
        "api_eSlot": [
            [37, 37, -1, -1, -1],
            [122, 106, 40, -1, -1],
            [75, 75, -1, -1, -1],
            [122, 106, 40, -1, -1],
            [75, 75, 129, -1, -1],
            [267, 15, 45, -1, -1],
        ],
        "api_e_effect_list": [[0], [0], [0], [0], [0], [0]],
        "api_f_maxhps": [93, 78, 54, 38, 7, 17],
        "api_f_nowhps": [93, 78, 54, 38, 7, 17],
        "api_fParam": api_fParam,
        "api_f_maxhps": api_f_maxhps,
        "api_f_nowhps": api_f_maxhps,
        "api_formation": [api_formation_id, 1, 3],  # 阵型选择
        "api_hougeki1": None,
        "api_hougeki2": None,
        "api_hougeki3": None,
        "api_hourai_flag": [1, 1, 0, 0],  # 炮雷战flag
        "api_kouku": {},  # 航空战相关信息
        "api_midnight_flag": 0,  # 夜战flag
        "api_opening_atack": {},  # 开幕战信息
        "api_opening_flag": 1,  # 开幕战flag
        "api_opening_taisen": None,  # 开幕反潜信息
        "api_opening_taisen": 0,  # 开幕反潜flag
        "api_raigeki": None,  # 雷击战信息
        "api_search": [],  # 索敌信息
        "api_ship_ke": [1002, 346, 706, 538, 649, 564],  # 敌方舰船信息
        "api_ship_lv": [99, 99, 99, 99, 98, 98],  # 敌方舰船等级
        "api_smoke_type": 0,
        "api_stage_flag": [],  # 战斗阶段flag
    }

    # mock data
    # api_data = PracticeService.battle()
    return create_response(api_data)


# 演习结果
@require_POST
def battle_result(request):
    api_data = PracticeService.battle_result()
    return create_response(api_data)
