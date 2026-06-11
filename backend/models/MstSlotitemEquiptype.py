from django.db import models


class MstSlotitemEquiptype(models.Model):
    api_id = models.IntegerField(primary_key=True)
    api_name = models.TextField(null=True, blank=True)
    api_show_flg = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "mst_slotitem_equiptype"

    def __str__(self):
        return str(self.api_id)
