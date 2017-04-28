from rest_framework import viewsets, permissions

from .models import DateScheduleItem, WeekScheduleItem
from .serializers import DateScheduleItemSerializer, WeekScheduleItemSerializer


class DateScheduleItemViewSet(viewsets.ModelViewSet):
    serializer_class = DateScheduleItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = DateScheduleItem.objects.all()


class WeekScheduleItemViewSet(viewsets.ModelViewSet):
    serializer_class = WeekScheduleItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = WeekScheduleItem.objects.all()