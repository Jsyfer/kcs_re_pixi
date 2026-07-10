from django.db import models


class Ship(models.Model):
    api_id = models.AutoField(primary_key=True)
    api_sortno = models.IntegerField(null=True, blank=True)
    api_ship_id = models.IntegerField(null=True, blank=True)
    api_lv = models.IntegerField()
    api_exp = models.JSONField()
    api_nowhp = models.IntegerField()
    api_maxhp = models.IntegerField()
    api_soku = models.IntegerField(null=True, blank=True)
    api_leng = models.IntegerField(null=True, blank=True)
    api_slot = models.JSONField()
    api_onslot = models.JSONField(null=True, blank=True)
    api_slot_ex = models.IntegerField(null=True, blank=True)
    api_kyouka = models.JSONField(null=True, blank=True)
    api_backs = models.IntegerField(null=True, blank=True)
    api_fuel = models.IntegerField()
    api_bull = models.IntegerField()
    api_slotnum = models.IntegerField(null=True, blank=True)
    api_ndock_time = models.IntegerField(null=True, blank=True)
    api_ndock_item = models.JSONField(null=True, blank=True)
    api_srate = models.IntegerField(null=True, blank=True)
    api_cond = models.IntegerField()
    api_karyoku = models.JSONField()
    api_raisou = models.JSONField()
    api_taiku = models.JSONField()
    api_soukou = models.JSONField()
    api_kaihi = models.JSONField()
    api_taisen = models.JSONField()
    api_sakuteki = models.JSONField()
    api_lucky = models.JSONField()
    api_locked = models.IntegerField(null=True, blank=True)
    api_locked_equip = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "ship"

    def __str__(self):
        return str(self.api_id)
