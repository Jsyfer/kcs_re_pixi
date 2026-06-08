from django.db import models


class MstFurniture(models.Model):
    api_id = models.IntegerField(primary_key=True)
    api_type = models.IntegerField(null=True, blank=True)
    api_no = models.IntegerField(null=True, blank=True)
    api_title = models.TextField(null=True, blank=True)
    api_description = models.TextField(null=True, blank=True)
    api_rarity = models.IntegerField(null=True, blank=True)
    api_price = models.IntegerField(null=True, blank=True)
    api_saleflg = models.IntegerField(null=True, blank=True)
    api_bgm_id = models.IntegerField(null=True, blank=True)
    api_version = models.IntegerField(null=True, blank=True)
    api_outside_id = models.IntegerField(null=True, blank=True)
    api_active_flag = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "mst_furniture"

    def __str__(self):
        return str(self.api_id)
