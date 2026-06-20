from django.forms.models import model_to_dict
from ..models.PresetItems import PresetItems
from django.conf import settings
import json


class PresetService:

    @staticmethod
    def get_preset_items():
        preset_items = PresetItems.objects.using(settings.KCS_DB).all()
        return [{k: v for k, v in model_to_dict(item).items() if v is not None} for item in preset_items]
