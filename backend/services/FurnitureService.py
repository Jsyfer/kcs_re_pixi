from django.forms.models import model_to_dict
from ..models.Furniture import Furniture
from django.conf import settings


class FurnitureService:

    @staticmethod
    def get_furniture():
        furniture = Furniture.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in furniture]
