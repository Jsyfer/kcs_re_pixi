import json
from django.http import HttpResponse


def create_response(api_data):
    data = {
        "api_result": 1,
        "api_result_msg": "成功",
        "api_data": api_data,
    }

    return HttpResponse(
        "svdata=" + json.dumps(data, ensure_ascii=True), content_type="text/plain"
    )


def create_response_success():
    data = {
        "api_result": 1,
        "api_result_msg": "成功",
    }

    return HttpResponse(
        "svdata=" + json.dumps(data, ensure_ascii=True), content_type="text/plain"
    )
