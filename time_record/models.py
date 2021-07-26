from django.db import models


class ExitAndEnterTime(models.Model):

    date_of_user = models.CharField(max_length=150)
    month = models.CharField(max_length=100)
    enter_time = models.FloatField(default=0)
    exit_time = models.FloatField(default=0)
    attendance_time = models.FloatField()
