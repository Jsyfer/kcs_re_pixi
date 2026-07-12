from django.db import models


class Quest(models.Model):
    api_no = models.AutoField(primary_key=True)
    api_category = models.IntegerField()
    api_type = models.IntegerField()
    api_label_type = models.IntegerField()
    api_state = models.IntegerField()
    api_title = models.TextField(null=True, blank=True)
    api_detail = models.TextField(null=True, blank=True)
    api_voice_id = models.IntegerField()
    api_lost_badges = models.IntegerField()
    api_get_material = models.JSONField(null=True, blank=True)
    api_bonus_flag = models.IntegerField()
    api_progress_flag = models.IntegerField()
    api_invalid_flag = models.IntegerField()

    class Meta:
        db_table = "quest"

    def __str__(self):
        return str(self.api_no)
