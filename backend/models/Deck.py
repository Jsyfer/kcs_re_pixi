from django.db import models


class Deck(models.Model):
    api_preset_no = models.IntegerField(primary_key=True)
    api_name = models.TextField(null=True, blank=True)
    api_name_id = models.TextField(null=True, blank=True)
    api_ship = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = "deck"

    def __str__(self):
        return str(self.api_preset_no)
