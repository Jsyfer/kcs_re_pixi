from django.forms.models import model_to_dict
from ..models.Mission import Mission
from django.conf import settings


class MissionService:

    @staticmethod
    def get_mission():
        mission = Mission.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in mission]
