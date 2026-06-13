from django.forms.models import model_to_dict

from backend.models.MstBGM import MstBGM
from backend.models.MstFurniture import MstFurniture
from backend.models.MstMaparea import MstMaparea
from backend.models.MstMapbgm import MstMapbgm
from backend.models.MstMapinfo import MstMapinfo
from backend.models.MstMission import MstMission
from backend.models.MstPayitem import MstPayitem
from backend.models.MstShip import MstShip
from backend.models.MstShipgraph import MstShipgraph
from backend.models.MstShipupgrade import MstShipupgrade
from backend.models.MstSlotitem import MstSlotitem
from backend.models.MstSlotitemEquiptype import MstSlotitemEquiptype
from backend.models.MstStype import MstStype
from backend.models.MstUseitem import MstUseitem
from django.conf import settings

import json


class MstService:

    @staticmethod
    def get_mst_bgm():
        mst_bgm = MstBGM.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in mst_bgm]

    @staticmethod
    def get_mst_furniture():
        mst_furniture = MstFurniture.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in mst_furniture]

    @staticmethod
    def get_mst_maparea():
        mst_maparea = MstMaparea.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in mst_maparea]

    @staticmethod
    def get_mst_mapbgm():
        mst_mapbgm = MstMapbgm.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in mst_mapbgm]

    @staticmethod
    def get_mst_mapinfo():
        mst_mapinfo = MstMapinfo.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in mst_mapinfo]

    @staticmethod
    def get_mst_mission():
        mst_mission = MstMission.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in mst_mission]

    @staticmethod
    def get_mst_payitem():
        mst_payitem = MstPayitem.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in mst_payitem]

    @staticmethod
    def get_mst_ship():
        mst_ship = MstShip.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in mst_ship]

    @staticmethod
    def get_mst_ship_by_id(ship_id):
        mst_ship = MstShip.objects.using(settings.KCS_DB).get(api_id=ship_id)
        return mst_ship

    @staticmethod
    def get_mst_shipgraph():
        mst_shipgraph = MstShipgraph.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in mst_shipgraph]

    @staticmethod
    def get_mst_shipupgrade():
        mst_shipupgrade = MstShipupgrade.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in mst_shipupgrade]

    @staticmethod
    def get_mst_slotitem():
        mst_slotitem = MstSlotitem.objects.using(settings.KCS_DB).all()
        return [
            {k: v for k, v in model_to_dict(item).items() if v is not None}
            for item in mst_slotitem
        ]

    @staticmethod
    def get_mst_slotitem_by_id(item_id):
        mst_slotitem = MstSlotitem.objects.using(settings.KCS_DB).get(api_id=item_id)
        return mst_slotitem

    @staticmethod
    def get_mst_slotitem_equiptype():
        mst_slotitem_equiptype = MstSlotitemEquiptype.objects.using(
            settings.KCS_DB
        ).all()
        return [model_to_dict(item) for item in mst_slotitem_equiptype]

    @staticmethod
    def get_mst_stype():
        mst_stype = MstStype.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in mst_stype]

    @staticmethod
    def get_mst_useitem():
        mst_useitem = MstUseitem.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in mst_useitem]

    @staticmethod
    def get_mst_const():
        return json.load(open("backend/mst/api_mst_const.json", encoding="utf-8"))

    @staticmethod
    def get_mst_mst_equip_exslot():
        return json.load(
            open("backend/mst/api_mst_equip_exslot.json", encoding="utf-8")
        )

    @staticmethod
    def get_mst_mst_equip_exslot_ship():
        return json.load(
            open("backend/mst/api_mst_equip_exslot_ship.json", encoding="utf-8")
        )

    @staticmethod
    def get_mst_equip_limit_exslot():
        return json.load(
            open("backend/mst/api_mst_equip_limit_exslot.json", encoding="utf-8")
        )

    @staticmethod
    def get_mst_equip_ship():
        return json.load(open("backend/mst/api_mst_equip_ship.json", encoding="utf-8"))

    @staticmethod
    def get_mst_item_shop():
        return json.load(open("backend/mst/api_mst_item_shop.json", encoding="utf-8"))
