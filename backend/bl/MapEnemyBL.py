from django.forms.models import model_to_dict
from ..services.MapService import MapService
from django.conf import settings
import json
import random


# 海域点位业务逻辑
class MapEnemyBL:

    # 获取敌舰信息
    @staticmethod
    def get_enemy_info(map_point_info, ship_list):
        enemy_info_list = MapService.get_map_enemy(
            map_point_info.maparea_id, map_point_info.mapinfo_no, map_point_info.point_no
        )
        # TODO boss点的敌舰信息需要根据boss最终形态与否决定，暂时随机选择一个敌舰信息
        random_enemy_info_list = []
        for enemy_info in enemy_info_list:
            pattern = enemy_info.get("pattern")
            random_enemy_info_list.append(enemy_info)
        return random.choice(random_enemy_info_list)
