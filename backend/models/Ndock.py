from django.db import models


class Ndock(models.Model):
    api_member_id = models.IntegerField(null=True, blank=True)
    api_id = models.IntegerField(primary_key=True)
    api_state = models.IntegerField(null=True, blank=True)
    api_ship_id = models.IntegerField(null=True, blank=True)
    api_complete_time = models.IntegerField(null=True, blank=True)
    api_complete_time_str = models.TextField(null=True, blank=True)
    api_item1 = models.IntegerField(null=True, blank=True)
    api_item2 = models.IntegerField(null=True, blank=True)
    api_item3 = models.IntegerField(null=True, blank=True)
    api_item4 = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "ndock"

    def __str__(self):
        return str(self.api_id)
