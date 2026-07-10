from django.forms.models import model_to_dict
from ..models.Ship import Ship
from backend.models.MstShip import MstShip
from backend.models.MstShipgraph import MstShipgraph
from backend.models.MstShipupgrade import MstShipupgrade
from django.conf import settings


class ShipService:

    @staticmethod
    def get_ship():
        ships = Ship.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in ships]

    @staticmethod
    def get_ship_by_id(ship_id):
        return Ship.objects.using(settings.KCS_DB).get(api_id=ship_id)

    @staticmethod
    def check_ship_exists(ship_id):
        return Ship.objects.using(settings.KCS_DB).filter(api_id=ship_id).first()

    @staticmethod
    def del_ship_by_id(ship_id):
        Ship.objects.using(settings.KCS_DB).get(api_id=ship_id).delete()

    @staticmethod
    def create_ship(ship_dict):
        ship = Ship.objects.using(settings.KCS_DB).create(**ship_dict)
        return ship

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
