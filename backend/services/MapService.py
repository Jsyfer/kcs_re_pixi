from django.forms.models import model_to_dict
from ..models.MapInfo import MapInfo
from ..models.CurrentBattleInfo import CurrentBattleInfo
from django.conf import settings
import json
import random


class MapService:

    @staticmethod
    def get_map_info():
        map_info = MapInfo.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in map_info]

    # 判断是否要转罗盘
    @staticmethod
    def need_rashin(map_id, current_id):
        rashin = json.load(open(f"backend/mst/map_rashin/{map_id}.json", encoding="utf-8"))
        return rashin[current_id]["rashin_flg"]

    # 获取下一个分歧点位
    @staticmethod
    def get_next_map_point(map_id, current_id, ship_list):
        rashin = json.load(open(f"backend/mst/map_rashin/{map_id}.json", encoding="utf-8"))

        next_config = rashin[current_id]["next"]
        points = next_config["point"]
        probability = next_config["probabilities"]
        if "condition" in next_config:
            condition = next_config["condition"]
            if condition == "ship_count":
                probability = next_config["probabilities"][len(ship_list) - 1]

        return random.choices(points, weights=probability, k=1)[0]

    # 获取海域敌舰信息
    @staticmethod
    def get_map_enemy(map_id):
        return json.load(open(f"backend/mst/map_enemy/{map_id}.json", encoding="utf-8"))

    @staticmethod
    def set_current_battle_info(api_maparea_id, api_mapinfo_no, api_deck_id):
        # 删除当前出击信息
        CurrentBattleInfo.objects.using(settings.KCS_DB).all().delete()

        # 创建新的出击信息
        battle_info = CurrentBattleInfo(
            api_maparea_id=api_maparea_id,
            api_mapinfo_no=api_mapinfo_no,
            api_deck_id=api_deck_id,
        )
        battle_info.save(using=settings.KCS_DB)

    @staticmethod
    def get_current_battle_info():
        return CurrentBattleInfo.objects.using(settings.KCS_DB).get()
