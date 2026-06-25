from django.forms.models import model_to_dict
from ..models.Material import Material
from django.conf import settings


class MaterialService:

    @staticmethod
    def get_material():
        return Material.objects.using(settings.KCS_DB).get(id=2005354)

    @staticmethod
    def get_material_by_id(api_id):
        material = Material.objects.using(settings.KCS_DB).get(api_id=api_id)
        return material

    @staticmethod
    def get_material_list():
        material = Material.objects.using(settings.KCS_DB).get(id=2005354)
        return [
            {
                "api_id": 1,
                "api_member_id": material.id,
                "api_value": material.fuel,
            },
            {
                "api_id": 2,
                "api_member_id": material.id,
                "api_value": material.bull,
            },
            {
                "api_id": 3,
                "api_member_id": material.id,
                "api_value": material.steel,
            },
            {
                "api_id": 4,
                "api_member_id": material.id,
                "api_value": material.aluminium,
            },
            {
                "api_id": 5,
                "api_member_id": material.id,
                "api_value": material.construction,
            },
            {
                "api_id": 6,
                "api_member_id": material.id,
                "api_value": material.repair,
            },
            {
                "api_id": 7,
                "api_member_id": material.id,
                "api_value": material.development,
            },
            {
                "api_id": 8,
                "api_member_id": material.id,
                "api_value": material.renovation,
            },
        ]
