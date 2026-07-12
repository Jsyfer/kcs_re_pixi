from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.forms.models import model_to_dict

from ..services.AdmiralService import AdmiralService
from ..services.FurnitureService import FurnitureService
from ..services.KdockService import KdockService
from ..services.SlotItemService import SlotItemService
from ..services.UseitemService import UseitemService
from ..services.DeckService import DeckService
from ..services.NdockService import NdockService
from ..services.MstService import MstService
from ..services.ShipService import ShipService
from ..services.AirBaseService import AirBaseService
from ..services.MapService import MapService
from ..services.PresetService import PresetService
from ..services.MaterialService import MaterialService
from ..services.PracticeService import PracticeService
from ..services.MissionService import MissionService
from ..services.QuestService import QuestService
from ..utils.Utils import Utils
from ..utils.GameUtils import GameUtils
from .common import create_response
from django.conf import settings


# 玩家数据获取
@require_POST
def require_info(request):
    admiralData = AdmiralService.get_admiral() or {}
    api_data = {
        "api_basic": {
            "api_member_id": admiralData.get("api_member_id"),
            "api_firstflag": admiralData.get("api_firstflag"),
        },
        "api_slot_item": SlotItemService.get_slot_items(),
        "api_unsetslot": SlotItemService.get_unset_slots(),
        "api_kdock": KdockService.get_kdock(),
        "api_useitem": UseitemService.get_useitem(),
        "api_furniture": FurnitureService.get_furniture(),
        "api_extra_supply": admiralData.get("api_extra_supply"),
        "api_oss_setting": {
            "api_language_type": admiralData.get("api_language_type"),
            "api_oss_items": admiralData.get("api_oss_items"),
        },
        "api_skin_id": admiralData.get("api_skin_id"),
        "api_position_id": admiralData.get("api_position_id"),
    }

    return create_response(api_data)


# 编成预设获取
@require_POST
def preset_deck(request):
    admiralData = AdmiralService.get_admiral() or {}
    api_data = {
        "api_deck": DeckService.get_deck(),
        "api_max_num": admiralData.get("api_max_deck"),
    }
    return create_response(api_data)


# 入渠按钮选择时相关信息获取
@require_POST
def ndock(request):
    ndock_list = NdockService.get_ndock()
    for ndock in ndock_list:
        # 判断是否有船在入渠
        if ndock["api_ship_id"] != 0:
            # 检查是否到达修理完成时间
            if Utils.check_if_time_passed(ndock["api_complete_time"]):
                ship = ShipService.get_ship_by_id(ndock["api_ship_id"])
                GameUtils.fix_ship_status(ship)
                ndockObj = NdockService.get_ndock_by_id(ndock["api_id"])
                ndockObj.api_ship_id = 0
                ndockObj.api_state = 0
                ndockObj.api_complete_time = 0
                ndockObj.api_complete_time_str = "0"
                # 更新入渠资源状态
                ndockObj.api_item1 = 0  # 燃料
                ndockObj.api_item2 = 0  # 钢材
                ndockObj.save()
    api_data = NdockService.get_ndock()
    return create_response(api_data)


# 工厂按钮选择时相关信息获取
@require_POST
def preset_dev_items(request):
    admiralData = AdmiralService.get_admiral() or {}
    api_data = {
        "api_max_num": admiralData.get("api_max_dev_items"),
    }
    return create_response(api_data)


# 母港选择出击按钮时各舰队制空/TP信息获取
@require_POST
def chart_additional_info(request):
    api_deck_param = []
    deck_port = DeckService.get_deck_port()
    for deck in deck_port:
        deck_ship_equip_list = []
        deck_ship_list = []
        for ship_id in deck["api_ship"]:
            if ship_id != -1:
                ship = ShipService.get_ship_by_id(ship_id)
                mst_ship = MstService.get_mst_ship_by_id(ship.api_ship_id)
                deck_ship_list.append([ship, mst_ship])
                current_ship_equip_list = []
                for index, slot in enumerate(ship.api_slot or {}):
                    if slot != -1:
                        slot_item = SlotItemService.get_slot_item_by_id(slot)
                        mst_slotitem = MstService.get_mst_slotitem_by_id(slot_item.api_slotitem_id)
                        current_ship_equip_list.append([slot_item, mst_slotitem, (ship.api_onslot or [])[index]])
                deck_ship_equip_list.append(current_ship_equip_list)
        # 获取制空值
        seiku_value = GameUtils.get_tyku(deck_ship_equip_list)
        # 获取TP值
        tp_value = GameUtils.get_tp(deck_ship_list, deck_ship_equip_list)
        api_deck_param.append({"api_seiku_value": seiku_value["max"], "api_tp_value": tp_value["s"]})
    api_data = {"api_deck_param": api_deck_param}
    return create_response(api_data)


# 点击出击按钮获取出击海域以及陆航相关信息
@require_POST
def mapinfo(request):
    api_data = {
        "api_air_base": AirBaseService.get_air_base(),
        "api_air_base_expanded_info": AirBaseService.get_air_base_expanded_info(),
        "api_map_info": MapService.get_map_info(),
    }
    return create_response(api_data)


# 更换装备后，更新舰船信息
@require_POST
def ship3(request):
    api_data = {
        "api_deck_data": DeckService.get_deck_port(),
        "api_ship_data": [model_to_dict(ShipService.get_ship_by_id(request.POST.get("api_shipid")))],
        "api_slot_data": SlotItemService.get_unset_slots(),
    }
    return create_response(api_data)


# 显示装备预设面板
@require_POST
def preset_slot(request):
    api_data = {
        "api_max_num": (AdmiralService.get_admiral() or {}).get("api_count_preset_item"),
        "api_preset_items": PresetService.get_preset_slot(),
    }
    return create_response(api_data)


# 获取建造信息
@require_POST
def kdock(request):
    api_data = KdockService.get_kdock()
    return create_response(api_data)


# 获取资源信息
@require_POST
def material(request):
    api_data = MaterialService.get_material_list()
    return create_response(api_data)


# 获取资源信息
@require_POST
def slot_item(request):
    api_data = SlotItemService.get_slot_items()
    return create_response(api_data)


# 获取氪金道具
@require_POST
def payitem(request):
    api_data = {
        "api_useitem": UseitemService.get_useitem(),
    }
    return create_response(api_data)


# 获取提督信息，战绩
@require_POST
def record(request):
    admiral = AdmiralService.get_admiral_obj()
    api_mission_ratio = admiral.api_ms_success * 100 / admiral.api_ms_count
    api_practice_ratio = admiral.api_pt_win * 100 / (admiral.api_pt_win + admiral.api_pt_lose)
    api_war_ratio = admiral.api_st_win / (admiral.api_st_win + admiral.api_st_lose)
    api_data = {
        "api_air_base_expanded_info": AirBaseService.get_air_base_expanded_info(),
        "api_cmt": admiral.api_comment,
        "api_cmt_id": admiral.api_comment_id,
        "api_complate": ["0.0", "0.0"],  # TODO
        "api_deck": admiral.api_count_deck,
        "api_experience": [admiral.api_experience, 0],  # TODO 提督经验计算
        "api_friend": 0,  # TODO
        "api_furniture": len(FurnitureService.get_furniture()),
        "api_kdoc": admiral.api_count_kdock,
        "api_large_dock": admiral.api_large_dock,
        "api_level": admiral.api_level,
        "api_material_max": 30750,  # TODO
        "api_member_id": admiral.api_member_id,
        "api_mission": {
            "api_count": admiral.api_ms_count,
            "api_rate": f"{api_mission_ratio:.2f}",
            "api_success": admiral.api_ms_success,
        },
        "api_ndoc": admiral.api_count_ndock,
        "api_nickname": admiral.api_nickname,
        "api_nickname_id": admiral.api_nickname_id,
        "api_photo_url": "",  # TODO
        "api_practice": {
            "api_lose": admiral.api_pt_lose,
            "api_rate": f"{api_practice_ratio:.2f}",
            "api_win": admiral.api_pt_win,
        },
        "api_rank": admiral.api_rank,
        "api_ship": [len(ShipService.get_ship()), admiral.api_max_chara],
        "api_slotitem": [len(SlotItemService.get_slot_items()), admiral.api_max_slotitem],
        "api_war": {
            "api_lose": admiral.api_st_lose,
            "api_rate": f"{api_war_ratio:.2f}",
            "api_win": admiral.api_st_win,
        },
    }
    return create_response(api_data)


# 获取演习后补
@require_POST
def practice(request):
    api_data = PracticeService.get_practice_list()
    return create_response(api_data)


# 获取远征后补
@require_POST
def mission(request):
    api_data = {
        "api_limit_time": 1784084400,
        "api_list_items": MissionService.get_mission(),
    }
    return create_response(api_data)


# 获取当前出击舰队信息
@require_POST
def ship_deck(request):
    api_deck_rid = int(request.POST.get("api_deck_rid"))
    deck = DeckService.get_deck_port_by_id(api_deck_rid)
    api_ship_data = []
    for ship_id in deck.api_ship:
        if ship_id != -1:
            ship = ShipService.get_ship_by_id(ship_id)
            api_ship_data.append(model_to_dict(ship))

    api_data = {
        "api_ship_data": api_ship_data,
        "api_deck_data": [model_to_dict(deck)],
    }
    return create_response(api_data)


# 获取最新所持装备
@require_POST
def unsetslot(request):
    api_data = SlotItemService.get_unset_slots()
    return create_response(api_data)


# 获取最新家具信息
@require_POST
def furniture(request):
    api_data = FurnitureService.get_furniture()
    return create_response(api_data)


# 获取最新道具信息
@require_POST
def useitem(request):
    api_data = UseitemService.get_useitem()
    return create_response(api_data)


@require_POST
def questlist(request):
    """获取任务信息"""
    api_tab_id = int(request.POST.get("api_tab_id"))
    # TODO 任务筛选
    match api_tab_id:
        case 0:
            # 全 All
            pass
        case 1:
            # 日 Daily
            pass
        case 2:
            # 週 Weekly
            pass
        case 3:
            # 月 Monthly
            pass
        case 4:
            # 単 Once
            pass
        case 5:
            # 他 Others
            pass
        case 9:
            # 進行中任務
            pass
    questlist = QuestService.get_quest()
    api_data = {
        "api_count": len(questlist),
        "api_completed_kind": 0,
        "api_list": questlist,
        "api_exec_count": 0,
        "api_exec_type": 2502925,
    }
    return create_response(api_data)


# 活动海域出击condition
@require_POST
def sortie_conditions(request):
    # TODO 计算当前玩家的通常海域出击胜率
    # 部分大型限时活动（活动海域）会对玩家的出击胜率有硬性要求（通常要求在 75% 或 80% 以上）才能进入活动海域
    api_data = {"api_war": {"api_win": "174025", "api_lose": "5538", "api_rate": "0.97"}}
    return create_response(api_data)
