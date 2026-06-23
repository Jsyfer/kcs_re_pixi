from django.forms.models import model_to_dict
from ..models.Kdock import Kdock
from django.conf import settings


class KdockService:

    @staticmethod
    def get_kdock():
        kdock = Kdock.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in kdock]

    @staticmethod
    def get_kdock_by_id(dock_id):
        return Kdock.objects.using(settings.KCS_DB).get(api_id=dock_id)
