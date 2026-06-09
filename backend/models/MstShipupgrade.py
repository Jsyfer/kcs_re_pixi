from django.db import models


class MstShipupgrade(models.Model):
    api_id = models.IntegerField(null=True, blank=True)
    api_arms_mat_count = models.IntegerField(null=True, blank=True)
    api_aviation_mat_count = models.IntegerField(null=True, blank=True)
    api_catapult_count = models.IntegerField(null=True, blank=True)
    api_current_ship_id = models.IntegerField(null=True, blank=True)
    api_drawing_count = models.IntegerField(null=True, blank=True)
    api_original_ship_id = models.IntegerField(null=True, blank=True)
    api_report_count = models.IntegerField(null=True, blank=True)
    api_sortno = models.IntegerField(null=True, blank=True)
    api_tech_count = models.IntegerField(null=True, blank=True)
    api_upgrade_level = models.IntegerField(null=True, blank=True)
    api_upgrade_type = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "mst_shipupgrade"

    def __str__(self):
        return str(self.api_id)
