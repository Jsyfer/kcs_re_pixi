from django.forms.models import model_to_dict
from ..models.Useitem import Useitem
from django.conf import settings


class UseitemService:

    @staticmethod
    def get_useitem():
        useitems = Useitem.objects.using(settings.KCS_DB).all()
        return [model_to_dict(item) for item in useitems]
