from django.db import models


# 远征信息表
class Mission(models.Model):
    api_mission_id = models.IntegerField(primary_key=True)
    api_state = models.IntegerField()

    class Meta:
        db_table = "air_base"

    def __str__(self):
        return str(self.api_mission_id)
