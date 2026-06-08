from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from ..services.AdmiralService import AdmiralService
from .common import create_response


@require_POST
def get_option_setting(request):
    admiralData = AdmiralService.get_admiral_by_id(2005354) or {}
    api_data = {
        "api_skin_id": admiralData.get("api_skin_id", 0),
        "api_volume_setting": admiralData.get("api_volume_setting", 0),
    }

    return create_response(api_data)
