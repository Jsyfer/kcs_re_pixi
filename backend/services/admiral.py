# services/ship_service.py

from models.Admiral import Admiral


class AdmiralService:

    @staticmethod
    def get_admiral_by_id(admiral_id: int):
        return Admiral.objects.filter(api_id=admiral_id).first()
