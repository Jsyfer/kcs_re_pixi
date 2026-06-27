from django.db import models


class DeckPort(models.Model):
    api_id = models.IntegerField(primary_key=True)
    api_member_id = models.IntegerField(null=True, blank=True)
    api_name = models.TextField(null=True, blank=True)
    api_name_id = models.TextField(null=True, blank=True)
    api_mission = models.JSONField(null=True, blank=True)
    api_flagship = models.TextField(null=True, blank=True)
    api_ship = models.JSONField(default=list)

    class Meta:
        db_table = "deck_port"

    def __str__(self):
        return str(self.api_id)
