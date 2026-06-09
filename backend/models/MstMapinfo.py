from django.db import models


class MstMapinfo(models.Model):
    api_id = models.IntegerField(primary_key=True)
    api_maparea_id = models.IntegerField(null=True, blank=True)
    api_no = models.IntegerField(null=True, blank=True)
    api_name = models.TextField(null=True, blank=True)
    api_level = models.IntegerField(null=True, blank=True)
    api_opetext = models.TextField(null=True, blank=True)
    api_infotext = models.TextField(null=True, blank=True)
    api_item = models.JSONField()
    api_max_maphp = models.IntegerField(null=True, blank=True)
    api_required_defeat_count = models.IntegerField(null=True, blank=True)
    api_sally_flag = models.JSONField()

    class Meta:
        db_table = "mst_mapinfo"

    def __str__(self):
        return str(self.api_id)
