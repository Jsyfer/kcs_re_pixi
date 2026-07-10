from django.forms.models import model_to_dict
from .FShip import FShip
from ..services.MstService import MstService
from ..services.SlotItemService import SlotItemService
from ..services.ShipService import ShipService
from ..services.MapService import MapService
from django.conf import settings
import json
import random


# 战斗业务逻辑
class BattleBL:

    @staticmethod
    def init_f_ship_list(ship_list):
        f_ship_list = []
        """初始化我方舰队信息"""
        for index, ship_id in enumerate(ship_list):
            ship_info = ShipService.get_ship_by_id(ship_id)
            mst_ship_info = ShipService.get_mst_ship_by_id(ship_info.api_ship_id)
            f_ship = FShip(
                ship_id=ship_info.api_id,
                ship_idx=index,
                now_hp=ship_info.api_nowhp,
                max_hp=ship_info.api_maxhp,
                now_fuel=ship_info.api_fuel,
                max_fuel=ship_info.api_fuel,
                now_bull=ship_info.api_bull,
                max_bull=ship_info.api_bull,
                karyoku=ship_info.api_karyoku[0],
                raisou=ship_info.api_raisou[0],
                taiku=ship_info.api_taiku[0],
                soukou=ship_info.api_soukou[0],
                kaihi=ship_info.api_kaihi[0],
                taisen=ship_info.api_taisen[0],
                sakuteki=ship_info.api_sakuteki[0],
                lucky=ship_info.api_lucky[0],
                now_lv=ship_info.api_lv,
                max_lv=99 if ship_info.api_lv <= 99 else 185,
                now_exp=ship_info.api_exp[0],
                next_exp=ship_info.api_exp[1],
            )
            f_ship_list.append(f_ship)
        pass

    @staticmethod
    def get_direction():
        """获取交戦形態（1=同航战,2=反航战,3=T字有利,4=T字不利）"""
        # TODO 检查舰队是否有搭载彩云，有则回避T不利
        return random.choices([1, 2, 3, 4], weights=[0.45, 0.3, 0.15, 0.1], k=1)[0]

    @staticmethod
    def get_f_deck_info(ship_id_list):
        """获取我方编队信息"""
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

    @staticmethod
    def get_e_deck_info(ship_id_list):
        """获取敌舰编队信息"""
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

    @staticmethod
    def cal_sakuteki(ship_list):
        """计算索敌"""
        pass

    @staticmethod
    def get_sakuteki_result(ship_list):
        """TODO 获取索敌判定结果
        Args:
            ship_list: 舰船id list
        Returns:
            索敌判定结果
            `1`=Success, `2`=Success(Planes lost), `3`=Fail(Planes lost), `4`=Fail, `5`=Success(No planes used), `6`=Fail(No planes used)
        """
        sakuteki_value = 0
        sakuteki_bonus = 1
        for index, ship_id in enumerate(ship_list):
            if ship_id == -1:
                continue
            ship_info = ShipService.get_ship_by_id(ship_id)
            ship_sakuteki = ship_info.api_sakuteki[0]  # type: ignore
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
                if mst_slotitem_info.api_type[0] in [3, 5]:  # 判断是否为索敌装备 # type: ignore
                    if mst_slotitem_info.api_type[2] in [12, 13]:  # type: ignore
                        # TODO 装备为电探时，设置索敌倍率系数
                        sakuteki_bonus = 4
                    else:
                        # 装备为舰载机时
                        # TODO 判断舰载机索敌结果
                        return 5
        # 若无任何索敌装备 则单纯判定数值
        if sakuteki_value * sakuteki_bonus > 200:
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

    @staticmethod
    def is_day_first_attack():
        """TODO 判断是否进行1轮炮击战"""
        return True

    @staticmethod
    def is_day_second_attack():
        """TODO 判断是否进行2轮炮击战"""
        return False

    @staticmethod
    def cal_attack_order(f_ship_id_list, e_ship_id_list):
        """根据射程判断第一轮炮击战攻击顺序"""
        f_leng_list = []
        e_leng_list = []
        for index, ship_id in enumerate(f_ship_id_list):
            ship_info = ShipService.get_ship_by_id(ship_id)
            f_leng_list.append({"ship_idx": index, "ship_leng": ship_info.api_leng})
        for index, ship_id in enumerate(e_ship_id_list):
            mst_ship_info = ShipService.get_mst_ship_by_id(ship_id)
            e_leng_list.append({"ship_idx": index, "ship_leng": mst_ship_info.api_leng})
        # 为了保证最终呢排序结果中相同射程的舰船出手顺序随机，排序前先打乱列表
        random.shuffle(f_leng_list)
        random.shuffle(e_leng_list)
        # 进行排序
        f_attack_order = [item["ship_idx"] for item in sorted(f_leng_list, key=lambda x: x["ship_leng"], reverse=True)]
        e_attack_order = [item["ship_idx"] for item in sorted(e_leng_list, key=lambda x: x["ship_leng"], reverse=True)]
        return f_attack_order, e_attack_order

    @staticmethod
    def get_attack_target(defender_ship_list, attack_from):
        """获取攻击对象"""
        # TODO检查受攻击舰队是否存在潜艇，同时攻击舰艇舰种为可反潜舰种，则优先攻击潜艇

        defender_ship_id = random.choice(defender_ship_list)
        # TODO 随机到旗舰时，判定是否会被撩舰援护
        if attack_from == 0:
            return ShipService.get_ship_by_id(defender_ship_id), defender_ship_list.index(defender_ship_id)
        else:
            return ShipService.get_mst_ship_by_id(defender_ship_id), defender_ship_list.index(defender_ship_id)

    @staticmethod
    def cal_damage(attaker_ship, defender_ship, attack_from):
        """计算伤害"""
        if attack_from == 0:
            # 我方造成伤害
            damage = attaker_ship.api_karyoku[0] - defender_ship.api_souk[0]
        else:
            # 敌方造成伤害
            damage = attaker_ship.api_hong[0] - defender_ship.api_soukou[0]
        if damage < 0:
            return 0
        return damage

    @staticmethod
    def hougeki(f_ship_id_list, e_ship_id_list, f_attack_order, e_attack_order):
        """炮击战"""

        result_list = []
        for f_idx in f_attack_order:
            # 我方攻击
            f_atk_ship = ShipService.get_ship_by_id(f_ship_id_list[f_idx])
            e_def_ship, e_def_ship_idx = BattleBL.get_attack_target(e_ship_id_list, 0)
            f_damage = BattleBL.cal_damage(f_atk_ship, e_def_ship, 0)

            result_list.append(
                {
                    "at_eflag": 0,  # 攻击敌我双方区分
                    "at_idx": f_idx,  # 发起攻击舰船在各自舰队所处的位置
                    "at_type": 0,  # 攻击类型（0=普通攻击）
                    "df_idx": e_def_ship_idx,  # 受击舰船在各自舰队所处的位置
                    "equip_id": -1,  # 使用的装备ID
                    "critical": 1,  # 暴击标志（0=MISS，1=普通命中，2=暴击/Critical）
                    "damage": f_damage,  # 伤害量
                }
            )
            # 敌方攻击

        return 0

    # 判断昼战特殊攻击
    @staticmethod
    def is_day_special_attack():
        return 0

    # 计算炮击命中
    @staticmethod
    def cal_houg_meityu():
        return 0

    # 计算炮击回避
    @staticmethod
    def cal_houg_kaihi():
        return 0
