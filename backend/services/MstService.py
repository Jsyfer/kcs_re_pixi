from django.forms.models import model_to_dict

from backend.models.MstBGM import MstBGM
from backend.models.MstFurniture import MstFurniture
from django.conf import settings


class MstService:

    @staticmethod
    def get_mst_bgm():
        mst_bgm = MstBGM.objects.using(settings.KCS_DB).all()

        return [model_to_dict(item) for item in mst_bgm]

    @staticmethod
    def get_mst_furniture():
        mst_furniture = MstFurniture.objects.using(settings.KCS_DB).all()

        return [model_to_dict(item) for item in mst_furniture]
