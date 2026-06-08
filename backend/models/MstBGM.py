from django.db import models


class MstBGM(models.Model):
    api_id = models.IntegerField(primary_key=True)
    api_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "mst_bgm"

    def __str__(self):
        return str(self.api_id)
