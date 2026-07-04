from django.db import models


class MapEnemyInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    maparea_id = models.IntegerField()
    mapinfo_no = models.IntegerField()
    point_no = models.IntegerField()
    pattern = models.TextField(null=True, blank=True)
    enemy = models.JSONField()
    equip = models.JSONField(null=True, blank=True)
    exp = models.IntegerField()
    formation = models.IntegerField()
    deck_kind = models.IntegerField()

    class Meta:
        db_table = "map_enemy_info"

    def __str__(self):
        return str(self.id)
