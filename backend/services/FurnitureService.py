from django.forms.models import model_to_dict
from ..models.Furniture import Furniture
from django.conf import settings
import json


class FurnitureService:

    @staticmethod
    def get_furniture():
        furniture = Furniture.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in furniture]

    @staticmethod
    def get_furniture_affect_items():
        return json.load(
            open("backend/temp/api_furniture_affect_items.json", encoding="utf-8")
        )
