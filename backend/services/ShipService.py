from django.forms.models import model_to_dict
from ..models.Ship import Ship
from django.conf import settings


class ShipService:

    @staticmethod
    def get_ship():
        ships = Ship.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in ships]

    @staticmethod
    def get_ship_by_id(ship_id):
        ship = Ship.objects.using(settings.KCS_DB).get(api_id=ship_id)
        return ship
