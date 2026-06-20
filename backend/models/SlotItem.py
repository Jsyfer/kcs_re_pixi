from django.db import models


class SlotItem(models.Model):
    api_id = models.IntegerField(primary_key=True)
    api_slotitem_id = models.IntegerField()
    api_locked = models.IntegerField()
    api_level = models.IntegerField()
    api_alv = models.IntegerField()
    api_used_ship = models.IntegerField()
    api_used_air_base = models.IntegerField()

    class Meta:
        db_table = "slot_item"

    def __str__(self):
        return str(self.api_id)
