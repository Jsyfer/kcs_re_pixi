from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from ..services.AdmiralService import AdmiralService
from .common import create_response, create_response_success


# 战果画面（假）
@require_POST
def mxltvkpyuklh(request):
    api_data = {
        "api_count": 1000,
        "api_page_count": 100,
        "api_disp_page": 1,
        "api_list": [
            {
                "api_mxltvkpyuklh": 1,
                "api_mtjmdcwtvhdr": "Yuukyuuenn",
                "api_pbgkfylkbjuy": 0,
                "api_pcumlrymlujh": 1,
                "api_itbrdpdbkynm": "114514",
                "api_itslcqtmrxtf": 580260,
                "api_wuhnhojjxmke": 2218417542,
            },
            {
                "api_mxltvkpyuklh": 2,
                "api_mtjmdcwtvhdr": "和泉桃太",
                "api_pbgkfylkbjuy": 0,
                "api_pcumlrymlujh": 1,
                "api_itbrdpdbkynm": "野分組戦果部",
                "api_itslcqtmrxtf": 493476,
                "api_wuhnhojjxmke": 1744355448,
            },
            {
                "api_mxltvkpyuklh": 3,
                "api_mtjmdcwtvhdr": "さとり",
                "api_pbgkfylkbjuy": 0,
                "api_pcumlrymlujh": 1,
                "api_itbrdpdbkynm": "土曜まで休み！走れる！",
                "api_itslcqtmrxtf": 1182294,
                "api_wuhnhojjxmke": 6839182350,
            },
            {
                "api_mxltvkpyuklh": 4,
                "api_mtjmdcwtvhdr": "ぺこにゃん",
                "api_pbgkfylkbjuy": 0,
                "api_pcumlrymlujh": 1,
                "api_itbrdpdbkynm": "目指せ、初ランカー入り！",
                "api_itslcqtmrxtf": 1046786,
                "api_wuhnhojjxmke": 5726510460,
            },
            {
                "api_mxltvkpyuklh": 5,
                "api_mtjmdcwtvhdr": "カクサン",
                "api_pbgkfylkbjuy": 0,
                "api_pcumlrymlujh": 1,
                "api_itbrdpdbkynm": "ぺこにゃんさとりふぁいと",
                "api_itslcqtmrxtf": 1086525,
                "api_wuhnhojjxmke": 5595381792,
            },
            {
                "api_mxltvkpyuklh": 6,
                "api_mtjmdcwtvhdr": "ホロドモール",
                "api_pbgkfylkbjuy": 0,
                "api_pcumlrymlujh": 1,
                "api_itbrdpdbkynm": "進捗ダメです",
                "api_itslcqtmrxtf": 1064448,
                "api_wuhnhojjxmke": 4431463245,
            },
            {
                "api_mxltvkpyuklh": 7,
                "api_mtjmdcwtvhdr": "てっさん",
                "api_pbgkfylkbjuy": 0,
                "api_pcumlrymlujh": 1,
                "api_itbrdpdbkynm": "静かな海でありますように",
                "api_itslcqtmrxtf": 1142938,
                "api_wuhnhojjxmke": 3720512664,
            },
            {
                "api_mxltvkpyuklh": 8,
                "api_mtjmdcwtvhdr": "めや",
                "api_pbgkfylkbjuy": 0,
                "api_pcumlrymlujh": 1,
                "api_itbrdpdbkynm": "いいけどそろそろ大鳳をね",
                "api_itslcqtmrxtf": 1419024,
                "api_wuhnhojjxmke": 4436017740,
            },
            {
                "api_mxltvkpyuklh": 9,
                "api_mtjmdcwtvhdr": "munya",
                "api_pbgkfylkbjuy": 0,
                "api_pcumlrymlujh": 1,
                "api_itbrdpdbkynm": "そう、それは暗号だよ",
                "api_itslcqtmrxtf": 1132600,
                "api_wuhnhojjxmke": 3467104542,
            },
            {
                "api_mxltvkpyuklh": 10,
                "api_mtjmdcwtvhdr": "カルノウ",
                "api_pbgkfylkbjuy": 0,
                "api_pcumlrymlujh": 1,
                "api_itbrdpdbkynm": "ｚｚｚ、、、",
                "api_itslcqtmrxtf": 1258290,
                "api_wuhnhojjxmke": 3654940608,
            },
        ],
    }

    return create_response(api_data)
