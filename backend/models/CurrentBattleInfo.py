from django.db import models


class CurrentBattleInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    maparea_id = models.IntegerField()
    mapinfo_no = models.IntegerField()
    current_point = models.IntegerField()
    deck_id = models.IntegerField()
    enemy_info_id = models.IntegerField()

    class Meta:
        db_table = "current_battle_info"

    def __str__(self):
        return str(self.id)
