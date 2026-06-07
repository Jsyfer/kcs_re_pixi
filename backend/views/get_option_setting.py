import json
import time
from pathlib import Path

import requests
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render


@require_POST
def get_option_setting(request):
    data = {
        "api_result": 1,
        "api_result_msg": "成功",
        "api_data": {
            "api_skin_id": 102,
            "api_volume_setting": None,
        },
    }

    return HttpResponse(
        "svdata=" + json.dumps(data, ensure_ascii=True), content_type="text/plain"
    )
