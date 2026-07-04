from django.forms.models import model_to_dict

from ..services.MstService import MstService
from ..services.ShipService import ShipService
from ..services.MapService import MapService
from django.conf import settings
import json
import random


# 战斗结果业务逻辑
class BattleResultBL:

    # 计算经验值
    @staticmethod
    def cal_admiral_exp(rank, mst_mapinfo, map_point_info):
        base_exp = mst_mapinfo.admiral_exp
        base_exp_boss = mst_mapinfo.admiral_exp_boss
        if map_point_info.color_no == 5:
            match rank:
                case "S":
                    return base_exp
                case "A":
                    return int(base_exp * 0.8)
                case "B":
                    return int(base_exp * 0.5)
                case _:
                    return 0
        else:
            match rank:
                case "S":
                    return base_exp_boss
                case "A":
                    return int(base_exp_boss - base_exp * 0.5)
                case "B":
                    return int(base_exp_boss - base_exp * 0.8)
                case "C":
                    return base_exp
                case _:
                    return 0

    # 获取舰船exp信息
    @staticmethod
    def cal_ship_exp(ship_id_list, base_exp, mvp_ship_id, rank):
        exp = [-1] * 7

        match rank:
            case "S":
                rank_bonus = 1.2
            case "A":
                rank_bonus = 1.0
            case "B":
                rank_bonus = 1.0
            case "C":
                rank_bonus = 0.8
            case "D":
                rank_bonus = 0.7
            case _:
                rank_bonus = 0.5
        for index, ship_id in enumerate(ship_id_list):
            if ship_id == -1:
                continue
            flagship_bonus = 1.5 if index == 0 else 1
            mvp_bonus = 2 if (index + 1) == mvp_ship_id else 1

            exp[index + 1] = int(base_exp * rank_bonus * flagship_bonus * mvp_bonus)
        return exp

    # 计算舰船获取exp
    @staticmethod
    def get_ship_exp_info(ship_id_list):
        exp = []

        for ship_id in ship_id_list:
            if ship_id == -1:
                continue
            ship_info = ShipService.get_ship_by_id(ship_id)
            exp.append([ship_info.api_exp[0], ship_info.api_exp[0] + ship_info.api_exp[1]])  # type: ignore
        return exp

    # 获取掉落舰船信息
    @staticmethod
    def get_droped_ship(map_point_info):
        drop_ship_list = map_point_info.drop_ship
        if drop_ship_list is None or len(drop_ship_list) == 0:
            return None
        ship_no = random.choice(drop_ship_list)
        mst_ship = MstService.get_mst_ship_by_id(ship_no)
        ship_type = MstService.get_mst_stype_by_id(mst_ship.api_stype)
        return {
            "api_ship_id": mst_ship.api_id,
            "api_ship_type": ship_type.api_name,
            "api_ship_name": mst_ship.api_name,
            "api_ship_getmes": mst_ship.api_getmes,
        }
