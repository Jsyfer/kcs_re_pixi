from django.forms.models import model_to_dict
from ..models.MstBGM import MstBGM
from django.conf import settings


class MstService:

    @staticmethod
    def get_mst_bgm():
        mst_bgm = MstBGM.objects.using(settings.KCS_DB).all()

        return [model_to_dict(item) for item in mst_bgm]
