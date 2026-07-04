from django.forms.models import model_to_dict
from ..services.MapService import MapService
from django.conf import settings
import json
import random


def map_11(point_no, next_points, ship_list):
    match point_no:
        case 1:
            match len(ship_list):
                case 1:
                    return [0.2, 0.8]
                case 2:
                    return [0.25, 0.75]
                case 3:
                    return [0.3, 0.7]
                case 4:
                    return [0.35, 0.65]
                case 5:
                    return [0.4, 0.6]
                case 6:
                    return [0.45, 0.55]
                case _:
                    return [0.5, 0.5]
        case _:
            return [1 / len(next_points)] * len(next_points)


# 点位和概率
def get_probabilities(map_id, point_no, next_points, ship_list):
    ship_list = list(filter(lambda x: x != -1, ship_list))
    match map_id:
        case "11":
            return map_11(point_no, next_points, ship_list)
        case _:
            return [1 / len(next_points)] * len(next_points)


# 海域点位业务逻辑
class MapPointBL:

    # 获取下一个分歧点位
    @staticmethod
    def get_next_map_point(map_point_info, ship_list):
        next_points = map_point_info.next_points
        map_id = str(map_point_info.maparea_id) + str(map_point_info.mapinfo_no)
        if next_points is None or len(next_points) == 0:
            return None
        if len(next_points) == 1:
            return next_points[0]
        probabilities = get_probabilities(map_id, map_point_info.point_no, next_points, ship_list)
        return random.choices(next_points, weights=probabilities, k=1)[0]
