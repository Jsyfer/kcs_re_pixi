from django.db import models


class Material(models.Model):
    id = models.IntegerField(primary_key=True)
    fuel = models.IntegerField()
    bull = models.IntegerField()
    steel = models.IntegerField()
    aluminium = models.IntegerField()
    construction = models.IntegerField()
    repair = models.IntegerField()
    development = models.IntegerField()
    renovation = models.IntegerField()

    class Meta:
        db_table = "material"

    def __str__(self):
        return str(self.id)
