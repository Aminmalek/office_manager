from django.db.models import fields
from rest_framework import serializers
from . models import ExitAndEnterTime


class ExitAndEnterTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExitAndEnterTime
        fields = ['id','month','attendance_time']
