from datetime import datetime

from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from rest_framework import viewsets, permissions, views, response, status

from .models import DateScheduleItem, WeekScheduleItem, DAYS_OF_WEEK
from .serializers import DateScheduleItemSerializer, WeekScheduleItemSerializer


class DateScheduleItemViewSet(viewsets.ModelViewSet):
    serializer_class = DateScheduleItemSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = DateScheduleItem.objects.all()


class WeekScheduleItemViewSet(viewsets.ModelViewSet):
    serializer_class = WeekScheduleItemSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = WeekScheduleItem.objects.all()


class TemperatureViewSet(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        now = timezone.now()
        schedule_item = DateScheduleItem.objects.filter(start__lte=now, end__gte=now).first()
        if not schedule_item:
            schedule_item = WeekScheduleItem.objects.filter(
                day_of_week=DAYS_OF_WEEK[timezone.datetime.today().weekday()][0],
                start_time__lte=now.time(),
                end_time__gte=now.time(),
            ).first()
        if not schedule_item:
            return response.Response({'error':_('Object not found')}, status=status.HTTP_404_NOT_FOUND)
        return response.Response({'temperature': schedule_item.temperature})
