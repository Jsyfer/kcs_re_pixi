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
from django.conf import settings


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
        return [model_to_dict(item) for item in mst_slotitem]
