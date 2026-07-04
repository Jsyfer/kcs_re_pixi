from django.forms.models import model_to_dict

from ..services.MstService import MstService
from ..services.ShipService import ShipService
from ..services.MapService import MapService
from django.conf import settings
import json
import random


# 战斗业务逻辑
class BattleBL:

    # 获取航向（1=同航战,2=T字有利,3=反航战,4=T字不利）
    @staticmethod
    def get_direction(ship_list):
        # TODO 检查舰队是否有搭载彩云，有则回避T不利
        return random.choices([1, 2, 3, 4], weights=[0.45, 0.15, 0.3, 0.1], k=1)[0]

    # 获取我方编队信息
    @staticmethod
    def get_f_deck_info(ship_id_list):
        now_hp_info = []
        max_hp_info = []
        base_param = []
        for ship_id in ship_id_list:
            if ship_id == -1:
                continue
            ship_info = ShipService.get_ship_by_id(ship_id)
            now_hp_info.append(ship_info.api_nowhp)
            max_hp_info.append(ship_info.api_maxhp)
            base_param.append([ship_info.api_karyoku[0], ship_info.api_raisou[0], ship_info.api_taiku[0], ship_info.api_soukou[0]])  # type: ignore
        return {"now_hp_info": now_hp_info, "max_hp_info": max_hp_info, "base_param": base_param}

    # 获取敌舰编队信息
    @staticmethod
    def get_e_deck_info(ship_id_list):
        ship_lv = []
        hp_info = []
        base_param = []
        slot_item = []
        for ship_id in ship_id_list:
            if ship_id == -1:
                continue
            ship_info = MstService.get_mst_ship_by_id(ship_id)
            hp_info.append(ship_info.api_taik)
            ship_lv.append(1)  # TODO 敌舰等级，暂时返回1
            base_param.append([ship_info.api_houg, ship_info.api_raig, ship_info.api_tyku, ship_info.api_souk])
            slot_item.append(ship_info.init_item)
        return {
            "ship_lv": ship_lv,
            "now_hp_info": hp_info,
            "max_hp_info": hp_info,
            "base_param": base_param,
            "slot_item": slot_item,
        }
