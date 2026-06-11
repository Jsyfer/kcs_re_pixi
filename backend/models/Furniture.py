from django.db import models


class Furniture(models.Model):
    api_id = models.IntegerField(primary_key=True)
    api_furniture_type = models.IntegerField(null=True, blank=True)
    api_furniture_no = models.IntegerField(null=True, blank=True)
    api_furniture_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "furniture"

    def __str__(self):
        return str(self.api_id)
