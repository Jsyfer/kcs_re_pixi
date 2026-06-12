from django.db import models


class Material(models.Model):
    api_id = models.IntegerField(primary_key=True)
    api_member_id = models.IntegerField()
    api_value = models.IntegerField()

    class Meta:
        db_table = "material"

    def __str__(self):
        return str(self.api_id)
