from django.db import models


class MstUseitem(models.Model):
    api_id = models.IntegerField(primary_key=True)
    api_usetype = models.IntegerField(null=True, blank=True)
    api_category = models.IntegerField(null=True, blank=True)
    api_name = models.TextField(null=True, blank=True)
    api_description = models.JSONField(null=True, blank=True)
    api_price = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "mst_useitem"

    def __str__(self):
        return str(self.api_id)
