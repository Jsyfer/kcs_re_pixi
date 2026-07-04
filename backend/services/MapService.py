from django.forms.models import model_to_dict
from ..models.MapInfo import MapInfo
from ..models.CurrentBattleInfo import CurrentBattleInfo
from ..models.MapPointInfo import MapPointInfo
from django.conf import settings
import json
import random


class MapService:

    @staticmethod
    def get_map_info():
        map_info = MapInfo.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in map_info]

    @staticmethod
    def get_map_info_by_id(map_id):
        return MapInfo.objects.using(settings.KCS_DB).get(api_id=map_id)

    # 获取地图点位信息
    @staticmethod
    def get_map_point_info(api_maparea_id, api_mapinfo_no):
        map_point_info = MapPointInfo.objects.using(settings.KCS_DB).filter(
            maparea_id=api_maparea_id, mapinfo_no=api_mapinfo_no
        )
        cell_data = []
        for item in map_point_info:
            cell_data.append(
                {
                    "api_id": item.id,
                    "api_no": item.point_no,
                    "api_color_no": item.color_no,
                    "api_passed": item.passed,
                }
            )
        return cell_data

    # 获取特定点位信息
    @staticmethod
    def get_map_point_info_by_id(api_maparea_id, api_mapinfo_no, current_id):
        map_point_info = MapPointInfo.objects.using(settings.KCS_DB).get(
            maparea_id=api_maparea_id, mapinfo_no=api_mapinfo_no, point_no=current_id
        )
        return map_point_info

    # 获取Boss点位编号
    @staticmethod
    def get_bosscell_no(api_maparea_id, api_mapinfo_no):
        map_point_info = MapPointInfo.objects.using(settings.KCS_DB).get(
            maparea_id=api_maparea_id, mapinfo_no=api_mapinfo_no, color_no=5
        )
        return map_point_info

    # 获取海域敌舰信息
    @staticmethod
    def get_map_enemy(map_id):
        return json.load(open(f"backend/mst/map_enemy/{map_id}.json", encoding="utf-8"))

    @staticmethod
    def set_current_battle_info(maparea_id, mapinfo_no, current_point, deck_id):
        # 删除当前出击信息
        CurrentBattleInfo.objects.using(settings.KCS_DB).all().delete()

        # 创建新的出击信息
        battle_info = CurrentBattleInfo(
            maparea_id=maparea_id,
            mapinfo_no=mapinfo_no,
            current_point=current_point,
            deck_id=deck_id,
        )
        battle_info.save(using=settings.KCS_DB)

    @staticmethod
    def get_current_battle_info():
        return CurrentBattleInfo.objects.using(settings.KCS_DB).get()
