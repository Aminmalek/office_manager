from django.db.models.aggregates import Sum
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ExitAndEnterTimeSerializer
from . models import ExitAndEnterTime


class ExitEnterView(APIView):

    def post(self, request):

        date = self.request.data['date']
        month = self.request.data['month']
        enter = self.request.data['enter']
        exit = self.request.data['exit']

        if date and enter and exit and month:

            if float(exit) > float(enter):

                extime = int(float(exit))*60 + ((float(exit)*100) % 100)

                entime = int(float(enter))*60 + ((float(enter)*100) % 100)

                total = (extime - entime) / 60
                atten = int(float(total)) + ((float(total)*100) % 100)*0.006

                day_data = ExitAndEnterTime(date=date, month=month, enter_time=enter,
                                            exit_time=exit, attendance_time=atten)

                day_data.save()

                return Response({"content": "You submited your time succesfuly thank you!"},
                                status=status.HTTP_201_CREATED)

            else:
                return Response({"content": "please enter time in 24 hours format"},
                                status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):

        user_month = self.request.query_params.get('month')

        whole_month_time = ExitAndEnterTime.objects.filter(
            month__startswith=user_month)  # .aggregate(Sum('attendance_time'))

        atten_time = 0
        for values in whole_month_time.values():

            for k, v in values.items():
                if k == 'attendance_time':
                    atten_time += v
        total_time = round(atten_time, 3)

        return Response({"month": user_month, "total_workes_time": total_time}, status=status.HTTP_202_ACCEPTED)
