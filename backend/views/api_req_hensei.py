from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from ..services.AdmiralService import AdmiralService
from ..services.DeckService import DeckService
from .common import create_response_success
import json


# 编成更新时更新相关数据
@require_POST
def change(request):
    request_data = request.POST
    # 获取当前舰队的舰娘列表
    deck_port = DeckService.get_deck_port_by_id(request_data["api_id"])
    api_ship = deck_port.api_ship or []
    # 获取用于替换的舰娘id
    api_ship_id = int(request_data["api_ship_id"])
    # 获取被替换舰娘所在舰队的位置
    move_to_index = int(request_data["api_ship_idx"])
    if api_ship_id in api_ship:
        # 若目标舰娘属于当前舰队，则与被交换舰娘互换位置
        move_from_index = api_ship.index(api_ship_id)
        api_ship[move_from_index], api_ship[move_to_index] = (
            api_ship[move_to_index],
            api_ship[move_from_index],
        )
    else:
        all_decks = DeckService.get_deck_port()
        for deck in all_decks:
            # 若目标舰娘属于其它舰队，则用被替换舰娘更新所属舰队的对应位置
            if api_ship_id in deck.get("api_ship", []):
                move_from_index = deck["api_ship"].index(api_ship_id)
                move_to_ship_id = api_ship[move_to_index]
                deck["api_ship"][move_from_index] = move_to_ship_id
                DeckService.update_deck_port_by_id(
                    deck["api_id"], "api_ship", deck["api_ship"]
                )
                break
        # 更新当前舰队目标位置的舰娘
        api_ship[move_to_index] = api_ship_id
    # 更新当前舰队的舰娘列表
    DeckService.update_deck_port_by_id(request_data["api_id"], "api_ship", api_ship)

    return create_response_success()
