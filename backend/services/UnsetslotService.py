from django.forms.models import model_to_dict
from ..models.SlotItem import SlotItem
from django.conf import settings
import json


class UnsetslotService:

    @staticmethod
    def get_unset_slots():
        return json.load(open("backend/temp/api_unsetslot.json", encoding="utf-8"))
