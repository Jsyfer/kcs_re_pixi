from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST

from ..services.AdmiralService import AdmiralService
from ..services.DeckService import DeckService
from ..services.FurnitureService import FurnitureService
from ..services.LogService import LogService
from ..services.MaterialService import MaterialService
from ..services.NdockService import NdockService
from ..services.ShipService import ShipService
from ..services.PracticeService import PracticeService
from .common import create_response
from django.conf import settings


# 切换演习后补
@require_POST
def change_matching_kind(request):
    api_selected_kind = int(request.POST.get("api_selected_kind"))
    api_data = {"api_update_flag": api_selected_kind}
    return create_response(api_data)


# 开始演习
@require_POST
def battle(request):
    api_deck_id = int(request.POST.get("api_deck_id"))
    api_formation_id = int(request.POST.get("api_formation_id"))
    api_enemy_id = int(request.POST.get("api_enemy_id"))
    api_data = PracticeService.battle()
    return create_response(api_data)


# 演习结果
@require_POST
def battle_result(request):
    api_data = PracticeService.battle_result()
    return create_response(api_data)
