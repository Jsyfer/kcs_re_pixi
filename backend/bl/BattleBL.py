from django.forms.models import model_to_dict

from ..services.MstService import MstService
from ..services.SlotItemService import SlotItemService
from ..services.ShipService import ShipService
from ..services.MapService import MapService
from django.conf import settings
import json
import random


# 战斗业务逻辑
class BattleBL:

    # 获取航向（1=同航战,2=反航战,3=T字有利,4=T字不利）
    @staticmethod
    def get_direction(ship_list):
        # TODO 检查舰队是否有搭载彩云，有则回避T不利
        return random.choices([1, 2, 3, 4], weights=[0.45, 0.3, 0.15, 0.1], k=1)[0]

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

    # 计算索敌
    @staticmethod
    def cal_sakuteki(ship_list):
        return 0

    @staticmethod
    def is_sakuteki_success(ship_list):
        """判断索敌是否成功
        Args:
            ship_list: 舰船id list
        Returns:
            索敌判定结果 TODO
            `1`=Success, `2`=Success(Planes lost), `3`=Fail(Planes lost), `4`=Fail, `5`=Success(No planes used), `6`=Fail(No planes used)
        """
        sakuteki_value = 0
        sakuteki_bonus = 1
        for index, ship_id in enumerate(ship_list):
            if ship_id == -1:
                continue
            ship_info = ShipService.get_ship_by_id(ship_id)
            ship_sakuteki = ship_info.api_sakuteki[0]
            if index == 0:
                sakuteki_value += int(ship_sakuteki * 0.5)
            elif index == 1:
                sakuteki_value += int(ship_sakuteki * 0.2)
            else:
                sakuteki_value += int(ship_sakuteki * 0.125)
            for item_id in ship_info.api_slot:
                if item_id == -1:
                    continue
                item_info = SlotItemService.get_slot_item_by_id(item_id)
                mst_slotitem_info = MstService.get_mst_slotitem_by_id(item_info.api_slotitem_id)
                if mst_slotitem_info.api_type[0] in [3, 5]:  # 判断是否为索敌装备
                    if mst_slotitem_info.api_type[2] in [12, 13]:
                        # TODO 装备为电探时，设置索敌倍率系数
                        sakuteki_bonus = 3
                    else:
                        # 装备为舰载机时
                        # TODO 判断舰载机索敌结果
                        return 5
        # 若无任何索敌装备 则单纯判定数值
        if sakuteki_value * sakuteki_bonus > 250:
            return 1
        return 4

    # 计算制空
    @staticmethod
    def cal_seiku():
        return 0

    # 计算对潜
    @staticmethod
    def cal_taisen():
        return 0

    # 判断是否先制对潜
    @staticmethod
    def is_pre_taisen():
        return 0

    # 判断是否开幕雷击
    @staticmethod
    def is_pre_raigeiki():
        return 0

    # 判断交战形态（同航战，反航战，T字有利，T字不利）
    @staticmethod
    def which_kousen_keitai():
        return 0

    # 判断是否进行炮击战

    # 判断昼战特殊攻击
    @staticmethod
    def is_day_special_attack():
        return 0

    # 判断是否进行二轮炮击
    @staticmethod
    def is_day_second_attack():
        return 0

    # 计算炮击命中
    @staticmethod
    def cal_houg_meityu():
        return 0

    # 计算炮击回避
    @staticmethod
    def cal_houg_kaihi():
        return 0

    # 根据射程判断第一轮炮击战攻击顺序
    @staticmethod
    def cal_attack_order():
        return 0
