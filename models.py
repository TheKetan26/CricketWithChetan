from django.db import models


class Matches(models.Model):
    date = models.CharField(max_length=12)
    base_type = models.CharField(max_length=13)
    type = models.CharField(max_length=3)
    gender = models.CharField(max_length=6)
    match_id = models.IntegerField(primary_key=True)
    teams = models.CharField(max_length=128)

    def __str__(self):
        return str(self.match_id) + ' - ' + str(self.teams)
