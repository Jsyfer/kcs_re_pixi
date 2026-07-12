from django.forms.models import model_to_dict
from ..models.Quest import Quest
from django.conf import settings


class QuestService:

    @staticmethod
    def get_quest():
        quest = Quest.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in quest]
