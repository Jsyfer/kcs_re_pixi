from django.forms.models import model_to_dict
from ..models.Ndock import Ndock
from django.conf import settings


class NdockService:

    @staticmethod
    def get_ndock():
        ndock = Ndock.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in ndock]
