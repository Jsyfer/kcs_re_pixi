from django.db import models


class MstPayitem(models.Model):
    api_id = models.IntegerField(primary_key=True)
    api_description = models.TextField(null=True, blank=True)
    api_shop_description = models.TextField(null=True, blank=True)
    api_item = models.JSONField()
    api_name = models.TextField(null=True, blank=True)
    api_price = models.IntegerField(null=True, blank=True)
    api_type = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "mst_payitem"

    def __str__(self):
        return str(self.api_id)
