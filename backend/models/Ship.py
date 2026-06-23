from django.db import models


class Ship(models.Model):
    api_id = models.AutoField(primary_key=True)
    api_sortno = models.IntegerField(null=True, blank=True)
    api_ship_id = models.IntegerField(null=True, blank=True)
    api_lv = models.IntegerField(null=True, blank=True)
    api_exp = models.JSONField(null=True, blank=True)
    api_nowhp = models.IntegerField(null=True, blank=True)
    api_maxhp = models.IntegerField(null=True, blank=True)
    api_soku = models.IntegerField(null=True, blank=True)
    api_leng = models.IntegerField(null=True, blank=True)
    api_slot = models.JSONField()
    api_onslot = models.JSONField(null=True, blank=True)
    api_slot_ex = models.IntegerField(null=True, blank=True)
    api_kyouka = models.JSONField(null=True, blank=True)
    api_backs = models.IntegerField(null=True, blank=True)
    api_fuel = models.IntegerField(null=True, blank=True)
    api_bull = models.IntegerField(null=True, blank=True)
    api_slotnum = models.IntegerField(null=True, blank=True)
    api_ndock_time = models.IntegerField(null=True, blank=True)
    api_ndock_item = models.JSONField(null=True, blank=True)
    api_srate = models.IntegerField(null=True, blank=True)
    api_cond = models.IntegerField(null=True, blank=True)
    api_karyoku = models.JSONField(null=True, blank=True)
    api_raisou = models.JSONField(null=True, blank=True)
    api_taiku = models.JSONField(null=True, blank=True)
    api_soukou = models.JSONField(null=True, blank=True)
    api_kaihi = models.JSONField(null=True, blank=True)
    api_taisen = models.JSONField(null=True, blank=True)
    api_sakuteki = models.JSONField(null=True, blank=True)
    api_lucky = models.JSONField(null=True, blank=True)
    api_locked = models.IntegerField(null=True, blank=True)
    api_locked_equip = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "ship"

    def __str__(self):
        return str(self.api_id)
