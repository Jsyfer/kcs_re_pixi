from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from ..services.AdmiralService import AdmiralService
from .common import create_response


@require_POST
def get_incentive(request):
    admiralData = AdmiralService.get_admiral_by_id(2005354) or {}
    api_data = {"api_count": admiralData.get("api_count", 0)}

    return create_response(api_data)


@require_POST
def set_oss_condition(request):
    api_data = {"api_result": 1, "api_result_msg": "成功"}

    return create_response(api_data)
