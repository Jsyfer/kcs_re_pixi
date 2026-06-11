from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST

from ..services.AdmiralService import AdmiralService
from ..services.FurnitureService import FurnitureService
from ..services.KdockService import KdockService
from .common import create_response
from django.conf import settings


@require_POST
def require_info(request):

    api_data = {
        "api_basic": AdmiralService.get_admiral_fields(
            settings.MEMBER_ID, ["api_firstflag", "api_member_id"]
        ),
        "api_extra_supply": AdmiralService.get_admiral_fields(
            settings.MEMBER_ID, ["api_extra_supply"]
        ),
        "api_furniture": FurnitureService.get_furniture(),
        "api_kdock": KdockService.get_kdock(),
    }

    return create_response(api_data)
