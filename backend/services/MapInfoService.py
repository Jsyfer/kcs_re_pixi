from django.forms.models import model_to_dict
from ..models.MapInfo import MapInfo
from django.conf import settings


class MapInfoService:

    @staticmethod
    def get_map_info():
        map_info = MapInfo.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in map_info]
