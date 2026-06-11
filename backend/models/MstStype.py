from django.db import models


class MstStype(models.Model):
    api_id = models.IntegerField(primary_key=True)
    api_sortno = models.IntegerField(null=True, blank=True)
    api_name = models.TextField(null=True, blank=True)
    api_scnt = models.IntegerField(null=True, blank=True)
    api_kcnt = models.IntegerField(null=True, blank=True)
    api_equip_type = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = "mst_stype"

    def __str__(self):
        return str(self.api_id)
