from django.db import models


class PresetItems(models.Model):
    api_preset_no = models.IntegerField(primary_key=True)
    api_name = models.TextField(null=True, blank=True)
    api_selected_mode = models.IntegerField(null=True, blank=True)
    api_lock_flag = models.IntegerField(null=True, blank=True)
    api_slot_ex_flag = models.IntegerField(null=True, blank=True)
    api_slot_item = models.JSONField(null=True, blank=True)
    api_slot_item_ex = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = "preset_items"

    def __str__(self):
        return str(self.api_preset_no)
