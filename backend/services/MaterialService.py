from django.forms.models import model_to_dict
from ..models.Material import Material
from django.conf import settings


class MaterialService:

    @staticmethod
    def get_material():
        materials = Material.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in materials]
