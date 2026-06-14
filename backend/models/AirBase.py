from django.db import models


class AirBase(models.Model):
    id = models.AutoField(primary_key=True)
    api_area_id = models.IntegerField(null=True, blank=True)
    api_rid = models.IntegerField(null=True, blank=True)
    api_name = models.TextField(null=True, blank=True)
    api_distance = models.JSONField(null=True, blank=True)
    api_action_kind = models.IntegerField(null=True, blank=True)
    api_plane_info = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = "air_base"

    def __str__(self):
        return str(self.id)
