from django.forms.models import model_to_dict
from ..models.MapInfo import MapInfo
from django.conf import settings
import json


class MapService:

    @staticmethod
    def get_map_info():
        map_info = MapInfo.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in map_info]

    # 获取海域敌舰信息
    @staticmethod
    def get_map_enemy(map_id):
        return json.load(open(f"backend/mst/map_enemy/{map_id}.json", encoding="utf-8"))

    # 获取下一个分歧点位
    @staticmethod
    def get_next_map_point(map_id, current_id):
        return 0
