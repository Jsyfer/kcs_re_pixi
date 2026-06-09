from django.db import models


class MstMission(models.Model):

    api_id = models.IntegerField(primary_key=True)
    api_disp_no = models.IntegerField(null=True, blank=True)
    api_maparea_id = models.IntegerField(null=True, blank=True)
    api_name = models.TextField(null=True, blank=True)
    api_details = models.TextField(null=True, blank=True)
    api_reset_type = models.IntegerField(null=True, blank=True)
    api_damage_type = models.IntegerField(null=True, blank=True)
    api_time = models.IntegerField(null=True, blank=True)
    api_deck_num = models.IntegerField(null=True, blank=True)
    api_difficulty = models.IntegerField(null=True, blank=True)
    api_use_fuel = models.FloatField(null=True, blank=True)
    api_use_bull = models.IntegerField(null=True, blank=True)
    api_win_item1 = models.TextField(null=True, blank=True)
    api_win_item2 = models.TextField(null=True, blank=True)
    api_win_mat_level = models.TextField(null=True, blank=True)
    api_return_flag = models.IntegerField(null=True, blank=True)
    api_sample_fleet = models.JSONField()

    class Meta:
        db_table = "mst_mission"

    def __str__(self):
        return str(self.api_id)
