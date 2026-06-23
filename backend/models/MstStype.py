from django.db import models


class MstStype(models.Model):
    api_id = models.IntegerField(primary_key=True)
    api_sortno = models.IntegerField()
    api_name = models.TextField()
    api_scnt = models.IntegerField()
    api_kcnt = models.IntegerField()
    api_equip_type = models.JSONField()

    class Meta:
        db_table = "mst_stype"

    def __str__(self):
        return str(self.api_id)
