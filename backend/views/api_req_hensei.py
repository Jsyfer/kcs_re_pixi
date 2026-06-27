from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.forms.models import model_to_dict
from ..services.AdmiralService import AdmiralService
from ..services.DeckService import DeckService
from ..services.ShipService import ShipService
from .common import create_response, create_response_success
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
    if api_ship_id == -2:
        # 伴随舰一括解除
        first_ship_id = api_ship[0]
        api_ship = [-1] * 6
        api_ship[0] = first_ship_id
    else:
        # 通常交换
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
                    DeckService.update_deck_port_by_id(deck["api_id"], "api_ship", deck["api_ship"])
                    break
            # 更新当前舰队目标位置的舰娘
            api_ship[move_to_index] = api_ship_id
    # 更新当前舰队的舰娘列表
    DeckService.update_deck_port_by_id(request_data["api_id"], "api_ship", api_ship)

    return create_response_success()


# 记录编成预设
@require_POST
def preset_register(request):
    api_deck_id = int(request.POST["api_deck_id"])
    api_preset_no = int(request.POST["api_preset_no"])
    api_name = request.POST["api_name"]
    api_name_id = request.POST["api_name_id"]

    deck_port = DeckService.get_deck_port_by_id(api_deck_id)
    deck = DeckService.create_or_update_deck_by_id(api_preset_no, api_name, api_name_id, deck_port.api_ship)
    api_data = model_to_dict(deck)
    return create_response(api_data)


# 展开编成预设
@require_POST
def preset_select(request):
    api_deck_id = int(request.POST["api_deck_id"])
    api_preset_no = int(request.POST["api_preset_no"])

    deck_port = DeckService.get_deck_port_by_id(api_deck_id)
    deck = DeckService.get_deck_by_id(api_preset_no)
    # 检查舰船是否存在
    ship_list = []
    for ship_id in deck.api_ship:
        ship = ShipService.get_ship_by_id(ship_id)
        if ship:
            ship_list.append(ship_id)

    deck_port.api_ship = [-1] * 6
    deck_port.api_ship[: len(ship_list)] = ship_list
    deck_port.save()
    api_data = model_to_dict(deck_port)
    return create_response(api_data)


# 删除编成预设
@require_POST
def preset_delete(request):
    api_preset_no = int(request.POST["api_preset_no"])

    DeckService.delete_deck_by_id(api_preset_no)

    return create_response_success()
