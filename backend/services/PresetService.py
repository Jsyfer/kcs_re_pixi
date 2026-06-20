from django.forms.models import model_to_dict
from ..models.PresetSlot import PresetSlot
from django.conf import settings
import json


class PresetService:

    @staticmethod
    def get_preset_slot():
        preset_slot = PresetSlot.objects.using(settings.KCS_DB).all()
        return [{k: v for k, v in model_to_dict(item).items() if v is not None} for item in preset_slot]

    @staticmethod
    def get_preset_slot_by_id(slot_id):
        preset_slot = PresetSlot.objects.using(settings.KCS_DB).get(api_preset_no=slot_id)
        return preset_slot
