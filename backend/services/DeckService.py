from django.forms.models import model_to_dict
from ..models.Deck import Deck
from ..models.DeckPort import DeckPort
from django.conf import settings


class DeckService:

    @staticmethod
    def get_deck():
        decks = Deck.objects.using(settings.KCS_DB).all()
        result = {}
        for deck in decks:
            data = model_to_dict(deck)
            deck_id = str(data.pop("id"))
            result[deck_id] = data
        return result

    @staticmethod
    def get_deck_port():
        deck_ports = DeckPort.objects.using(settings.KCS_DB).all()
        return [model_to_dict(port) for port in deck_ports]

    @staticmethod
    def get_deck_port_by_id(deck_port_id):
        deck_port = DeckPort.objects.using(settings.KCS_DB).get(api_id=deck_port_id)
        return deck_port

    @staticmethod
    def update_deck_port_by_id(deck_port_id, update_key, update_value):
        DeckPort.objects.using(settings.KCS_DB).filter(api_id=deck_port_id).update(
            **{update_key: update_value}
        )
