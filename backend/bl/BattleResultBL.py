from django.forms.models import model_to_dict

from ..services.MstService import MstService
from ..services.ShipService import ShipService
from ..services.MapService import MapService
from django.conf import settings
import json
import random


# 战斗结果业务逻辑
class BattleResultBL:

    # 获取航向（1=同航战,2=T字有利,3=反航战,4=T字不利）
    @staticmethod
    def cal_exp(rank, base_exp):
        # TODO 检查舰队是否有搭载彩云，有则回避T不利
        return random.choices([1, 2, 3, 4], weights=[0.45, 0.15, 0.3, 0.1], k=1)[0]
