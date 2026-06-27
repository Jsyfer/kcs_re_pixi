from django.db import models


class MstEquipBonus(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    ship_id = models.JSONField(null=True, default=[])
    ship_class = models.JSONField(null=True, default=[])
    item_lv = models.IntegerField(null=True, default=0)
    karyoku = models.IntegerField(null=True, default=0)
    raisou = models.IntegerField(null=True, default=0)
    taiku = models.IntegerField(null=True, default=0)
    soukou = models.IntegerField(null=True, default=0)
    leng = models.IntegerField(null=True, default=0)
    soku = models.IntegerField(null=True, default=0)
    sakuteki = models.IntegerField(null=True, default=0)
    kaihi = models.IntegerField(null=True, default=0)
    taisen = models.IntegerField(null=True, default=0)

    class Meta:
        db_table = "mst_equip_bonus"

    def __str__(self):
        return str(self.id)
