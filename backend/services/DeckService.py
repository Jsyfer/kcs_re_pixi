from django.forms.models import model_to_dict
from ..models.Deck import Deck
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
