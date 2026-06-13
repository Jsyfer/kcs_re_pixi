from django.db import models


class MstSlotitem(models.Model):
    api_id = models.IntegerField(primary_key=True)
    api_sortno = models.IntegerField(null=True, blank=True)
    api_name = models.TextField(null=True, blank=True)
    api_type = models.JSONField(null=True, blank=True)
    api_taik = models.IntegerField(null=True, blank=True)
    api_souk = models.IntegerField(null=True, blank=True)
    api_houg = models.IntegerField(null=True, blank=True)
    api_raig = models.IntegerField(null=True, blank=True)
    api_soku = models.IntegerField(null=True, blank=True)
    api_baku = models.IntegerField(null=True, blank=True)
    api_tyku = models.IntegerField(null=True, blank=True)
    api_tais = models.IntegerField(null=True, blank=True)
    api_atap = models.IntegerField(null=True, blank=True)
    api_houm = models.IntegerField(null=True, blank=True)
    api_raim = models.IntegerField(null=True, blank=True)
    api_houk = models.IntegerField(null=True, blank=True)
    api_raik = models.IntegerField(null=True, blank=True)
    api_bakk = models.IntegerField(null=True, blank=True)
    api_saku = models.IntegerField(null=True, blank=True)
    api_sakb = models.IntegerField(null=True, blank=True)
    api_luck = models.IntegerField(null=True, blank=True)
    api_leng = models.IntegerField(null=True, blank=True)
    api_cost = models.IntegerField(null=True, blank=True)
    api_distance = models.IntegerField(null=True, blank=True)
    api_rare = models.IntegerField(null=True, blank=True)
    api_broken = models.JSONField(null=True, blank=True)
    api_usebull = models.TextField(null=True, blank=True)
    api_version = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "mst_slotitem"

    def __str__(self):
        return str(self.api_id)
