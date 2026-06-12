from django.db import models


class Useitem(models.Model):
    api_id = models.IntegerField(primary_key=True)
    api_count = models.IntegerField()

    class Meta:
        db_table = "useitem"

    def __str__(self):
        return str(self.api_id)
