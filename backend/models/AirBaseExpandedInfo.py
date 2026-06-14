from django.db import models


class AirBaseExpandedInfo(models.Model):
    api_area_id = models.IntegerField(primary_key=True)
    api_maintenance_level = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "air_base_expanded_info"

    def __str__(self):
        return str(self.api_area_id)
