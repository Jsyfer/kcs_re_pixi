from django.db import models


class MstShip(models.Model):
    api_id = models.IntegerField(primary_key=True)
    api_sortno = models.IntegerField(null=True, blank=True)
    api_sort_id = models.IntegerField(null=True, blank=True)
    api_name = models.TextField(null=True, blank=True)
    api_yomi = models.TextField(null=True, blank=True)
    api_stype = models.IntegerField(null=True, blank=True)
    api_ctype = models.IntegerField(null=True, blank=True)
    api_afterlv = models.IntegerField(null=True, blank=True)
    api_aftershipid = models.TextField(null=True, blank=True)
    api_taik = models.JSONField(null=True, blank=True)
    api_souk = models.JSONField(null=True, blank=True)
    api_houg = models.JSONField(null=True, blank=True)
    api_raig = models.JSONField(null=True, blank=True)
    api_tyku = models.JSONField(null=True, blank=True)
    api_luck = models.JSONField(null=True, blank=True)
    api_soku = models.IntegerField(null=True, blank=True)
    api_leng = models.IntegerField(null=True, blank=True)
    api_slot_num = models.IntegerField(null=True, blank=True)
    api_maxeq = models.JSONField(null=True, blank=True)
    api_buildtime = models.IntegerField(null=True, blank=True)
    api_broken = models.JSONField(null=True, blank=True)
    api_powup = models.JSONField(null=True, blank=True)
    api_backs = models.IntegerField(null=True, blank=True)
    api_getmes = models.TextField(null=True, blank=True)
    api_afterfuel = models.IntegerField(null=True, blank=True)
    api_afterbull = models.IntegerField(null=True, blank=True)
    api_fuel_max = models.IntegerField(null=True, blank=True)
    api_bull_max = models.IntegerField(null=True, blank=True)
    api_voicef = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "mst_ship"

    def __str__(self):
        return str(self.api_id)
