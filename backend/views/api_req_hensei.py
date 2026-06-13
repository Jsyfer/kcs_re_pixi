from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from ..services.AdmiralService import AdmiralService
from ..services.DeckPortService import DeckPortService
from .common import create_response_success
import json


@require_POST
def change(request):
    request_data = request.POST
    deck_port = DeckPortService.get_deck_port_by_id(request_data["api_id"])

    api_ship = deck_port.api_ship or []
    api_ship_id = int(request_data["api_ship_id"])
    move_to_index = int(request_data["api_ship_idx"])
    if api_ship_id in api_ship:
        # If the ship is already in current deck, swap the positions
        move_from_index = api_ship.index(api_ship_id)
        api_ship[move_from_index], api_ship[move_to_index] = (
            api_ship[move_to_index],
            api_ship[move_from_index],
        )
    else:
        # check if ship in another deck
        all_decks = DeckPortService.get_deck_port()
        for deck in all_decks:
            if api_ship_id in deck.get("api_ship", []):
                move_from_index = deck["api_ship"].index(api_ship_id)
                move_to_ship_id = api_ship[move_to_index]
                deck["api_ship"][move_from_index] = move_to_ship_id
                DeckPortService.update_deck_port_by_id(
                    deck["api_id"], "api_ship", deck["api_ship"]
                )
                break
        api_ship[move_to_index] = api_ship_id

    DeckPortService.update_deck_port_by_id(request_data["api_id"], "api_ship", api_ship)

    return create_response_success()
