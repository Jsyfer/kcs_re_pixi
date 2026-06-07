import json
import time
from pathlib import Path

import requests
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render
from ..services.AdmiralService import AdmiralService


@require_POST
def get_option_setting(request):
    admiralData = AdmiralService.get_admiral_by_id(2005354) or {}
    data = {
        "api_result": 1,
        "api_result_msg": "成功",
        "api_data": {
            "api_skin_id": admiralData.get("api_skin_id", 0),
            "api_volume_setting": admiralData.get("api_volume_setting", 0),
        },
    }

    return HttpResponse(
        "svdata=" + json.dumps(data, ensure_ascii=True), content_type="text/plain"
    )
