from django.forms.models import model_to_dict
from ..models.Ndock import Ndock
from django.conf import settings


# 入渠处理
class NdockService:

    # 当前入渠状态
    @staticmethod
    def get_ndock():
        ndock = Ndock.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in ndock]

    @staticmethod
    def get_ndock_by_id(api_id):
        return Ndock.objects.using(settings.KCS_DB).get(api_id=api_id)
