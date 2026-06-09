from django.db import models


class MstMapbgm(models.Model):
    api_id = models.IntegerField(primary_key=True)
    api_boss_bgm = models.JSONField()
    api_map_bgm = models.JSONField()
    api_maparea_id = models.IntegerField()
    api_moving_bgm = models.IntegerField()
    api_no = models.IntegerField()

    class Meta:
        db_table = "mst_mapbgm"

    def __str__(self):
        return str(self.api_id)
