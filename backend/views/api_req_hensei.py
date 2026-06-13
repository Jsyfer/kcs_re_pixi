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

    move_from_index = api_ship.index(int(request_data["api_ship_id"]))
    move_to_index = int(request_data["api_ship_idx"])
    api_ship[move_from_index], api_ship[move_to_index] = (
        api_ship[move_to_index],
        api_ship[move_from_index],
    )

    DeckPortService.update_deck_port_by_id(request_data["api_id"], "api_ship", api_ship)

    return create_response_success()
