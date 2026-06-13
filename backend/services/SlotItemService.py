from django.forms.models import model_to_dict
from ..models.SlotItem import SlotItem
from django.conf import settings


class SlotItemService:

    @staticmethod
    def get_slot_items():
        slot_items = SlotItem.objects.using(settings.KCS_DB).all()
        return [
            {k: v for k, v in model_to_dict(item).items() if v is not None}
            for item in slot_items
        ]
