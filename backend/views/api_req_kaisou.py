from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from ..services.AdmiralService import AdmiralService
from .common import create_response


@require_POST
def can_preset_slot_select(request):
    # TODO : Implement actual logic to determine if preset slot selection is allowed
    api_data = {"api_flag": 1}

    return create_response(api_data)
