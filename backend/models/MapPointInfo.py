from django.db import models


class MapPointInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    maparea_id = models.IntegerField()
    mapinfo_no = models.IntegerField()
    point_no = models.IntegerField()
    passed = models.IntegerField()
    color_no = models.IntegerField()
    event_id = models.IntegerField()
    event_kind = models.IntegerField()
    rashin_flg = models.IntegerField()
    rashin_id = models.IntegerField()
    next_points = models.JSONField(null=True, blank=True)
    drop_ship = models.JSONField(null=True, blank=True)
    drop_item = models.JSONField(null=True, blank=True)
    wiki_name = models.TextField(null=True, blank=True)
    api_distance = models.IntegerField(null=True, blank=True)
    select_cells = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = "map_point_info"

    def __str__(self):
        return str(self.id)
