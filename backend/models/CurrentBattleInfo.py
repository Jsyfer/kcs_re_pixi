from django.db import models


class CurrentBattleInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    api_maparea_id = models.IntegerField()
    api_mapinfo_no = models.IntegerField()
    api_deck_id = models.TextField()

    class Meta:
        db_table = "current_battle_info"

    def __str__(self):
        return str(self.id)
