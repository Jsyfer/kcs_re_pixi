# services/ship_service.py

from django.forms.models import model_to_dict

from ..models.Admiral import Admiral

DB = "kcs_api"


class AdmiralService:

    @staticmethod
    def get_admiral_by_id(api_member_id: int):
        admiral = Admiral.objects.using(DB).filter(api_member_id=api_member_id).first()
        return model_to_dict(admiral) if admiral else None
