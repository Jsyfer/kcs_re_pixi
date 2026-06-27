from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from ..services.AdmiralService import AdmiralService
from ..services.PracticeService import PracticeService
from .common import create_response, create_response_success


@require_POST
def get_incentive(request):
    admiralData = AdmiralService.get_admiral_by_id(2005354) or {}
    api_data = {"api_count": admiralData.get("api_count", 0)}

    return create_response(api_data)


@require_POST
def set_oss_condition(request):
    api_data = {"api_result": 1, "api_result_msg": "成功"}

    return create_response(api_data)


# 更新提督签名信息 TODO 机制与其它kcsapi不同，暂时不可用
@require_POST
def updatecomment(request):
    admiral = AdmiralService.get_admiral_obj()
    admiral.api_comment = request.POST.get("api_cmt")
    admiral.api_comment_id = int(request.POST.get("api_cmt_id"))
    admiral.save()
    return create_response_success()


# 获取演习对手信息
@require_POST
def get_practice_enemyinfo(request):
    api_member_id = int(request.POST.get("api_member_id"))
    api_data = PracticeService.get_practice_enemyinfo_by_id(api_member_id)
    return create_response(api_data)
