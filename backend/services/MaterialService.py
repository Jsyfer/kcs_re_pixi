from django.forms.models import model_to_dict
from ..models.Material import Material
from django.conf import settings


class MaterialService:

    @staticmethod
    def get_material():
        return Material.objects.using(settings.KCS_DB).get(api_id=2005354)

    @staticmethod
    def get_material_by_id(api_id):
        material = Material.objects.using(settings.KCS_DB).get(api_id=api_id)
        return material
