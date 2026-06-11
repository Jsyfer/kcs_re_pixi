from django.forms.models import model_to_dict
from ..models.Admiral import Admiral
from django.conf import settings


class AdmiralService:

    @staticmethod
    def get_admiral_by_id(api_member_id: int):
        admiral = (
            Admiral.objects.using(settings.KCS_DB)
            .filter(api_member_id=api_member_id)
            .first()
        )
        return model_to_dict(admiral) if admiral else None

    @staticmethod
    def get_admiral_fields(api_member_id: int, fields: list):
        results = (
            Admiral.objects.using(settings.KCS_DB)
            .values(*fields)
            .filter(api_member_id=api_member_id)
            .first()
        )
        return results
