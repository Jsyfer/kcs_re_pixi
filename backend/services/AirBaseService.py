from django.forms.models import model_to_dict
from ..models.AirBase import AirBase
from ..models.AirBaseExpandedInfo import AirBaseExpandedInfo
from django.conf import settings


class AirBaseService:

    @staticmethod
    def get_air_base():
        air_base = AirBase.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in air_base]

    @staticmethod
    def get_air_base_expanded_info():
        air_base_expanded_info = AirBaseExpandedInfo.objects.using(
            settings.KCS_DB
        ).all()
        return [model_to_dict(item) for item in air_base_expanded_info]
