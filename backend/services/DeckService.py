from django.forms.models import model_to_dict
from ..models.Deck import Deck
from ..models.DeckPort import DeckPort
from django.conf import settings


# 编成服务
class DeckService:

    # 获取全部编队预设
    @staticmethod
    def get_deck():
        decks = Deck.objects.using(settings.KCS_DB).all()
        result = {}
        for deck in decks:
            data = model_to_dict(deck)
            deck_id = str(data.pop("id"))
            result[deck_id] = data
        return result

    # 获取编队预设
    @staticmethod
    def get_deck_by_id(api_preset_no):
        return Deck.objects.using(settings.KCS_DB).get(api_preset_no=api_preset_no)

    # 获取所有编队信息
    @staticmethod
    def get_deck_port():
        deck_ports = DeckPort.objects.using(settings.KCS_DB).all()
        return [model_to_dict(port) for port in deck_ports]

    # 获取编队信息
    @staticmethod
    def get_deck_port_by_id(deck_port_id):
        deck_port = DeckPort.objects.using(settings.KCS_DB).get(api_id=deck_port_id)
        return deck_port

    # 更新编队
    @staticmethod
    def update_deck_port_by_id(deck_port_id, update_key, update_value):
        DeckPort.objects.using(settings.KCS_DB).filter(api_id=deck_port_id).update(**{update_key: update_value})
