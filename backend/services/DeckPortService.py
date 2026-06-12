from django.forms.models import model_to_dict
from ..models.DeckPort import DeckPort
from django.conf import settings


class DeckPortService:

    @staticmethod
    def get_deck_port():
        deck_ports = DeckPort.objects.using(settings.KCS_DB).all()
        return [model_to_dict(port) for port in deck_ports]
