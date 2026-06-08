from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from ..services.AdmiralService import AdmiralService
from .common import create_response


@require_POST
def get_incentive(request):
    admiralData = AdmiralService.get_admiral_by_id(2005354) or {}
    api_data = {"api_count": admiralData.get("api_count", 0)}

    return create_response(api_data)
