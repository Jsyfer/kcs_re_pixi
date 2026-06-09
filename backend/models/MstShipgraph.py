from django.db import models


class MstShipgraph(models.Model):
    api_id = models.IntegerField(primary_key=True)
    api_filename = models.TextField(null=True, blank=True)
    api_battle_n = models.JSONField(null=True, blank=True)
    api_battle_d = models.JSONField(null=True, blank=True)
    api_boko_n = models.JSONField(null=True, blank=True)
    api_boko_d = models.JSONField(null=True, blank=True)
    api_kaisyu_n = models.JSONField(null=True, blank=True)
    api_kaisyu_d = models.JSONField(null=True, blank=True)
    api_kaizo_n = models.JSONField(null=True, blank=True)
    api_kaizo_d = models.JSONField(null=True, blank=True)
    api_map_n = models.JSONField(null=True, blank=True)
    api_map_d = models.JSONField(null=True, blank=True)
    api_ensyuf_n = models.JSONField(null=True, blank=True)
    api_ensyuf_d = models.JSONField(null=True, blank=True)
    api_ensyue_n = models.JSONField(null=True, blank=True)
    api_weda = models.JSONField(null=True, blank=True)
    api_wedb = models.JSONField(null=True, blank=True)
    api_pa = models.JSONField(null=True, blank=True)
    api_pab = models.JSONField(null=True, blank=True)
    api_version = models.JSONField(null=True, blank=True)
    api_sortno = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "mst_shipgraph"

    def __str__(self):
        return str(self.api_id)
