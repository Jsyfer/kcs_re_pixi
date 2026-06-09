from django.db import models


class MstMaparea(models.Model):
    api_id = models.IntegerField(primary_key=True)
    api_name = models.TextField(null=True, blank=True)
    api_type = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "mst_maparea"

    def __str__(self):
        return str(self.api_id)
