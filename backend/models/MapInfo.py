from django.db import models


class MapInfo(models.Model):
    api_id = models.AutoField(primary_key=True)
    api_cleared = models.IntegerField(null=True, blank=True)
    api_defeat_count = models.IntegerField(null=True, blank=True)
    api_required_defeat_count = models.IntegerField(null=True, blank=True)
    api_gauge_type = models.IntegerField(null=True, blank=True)
    api_gauge_num = models.IntegerField(null=True, blank=True)
    api_air_base_decks = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "map_info"

    def __str__(self):
        return str(self.api_id)
