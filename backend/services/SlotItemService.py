from django.forms.models import model_to_dict
from ..models.SlotItem import SlotItem
from django.conf import settings


class SlotItemService:

    @staticmethod
    def get_slot_items():
        slot_items = SlotItem.objects.using(settings.KCS_DB).all()
        result = []
        for item in slot_items:
            item_dict = model_to_dict(item)
            if item_dict.get("api_alv") is None:
                item_dict.pop("api_alv", None)
            result.append(item_dict)
        return result
