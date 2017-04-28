from rest_framework import serializers

from .models import DateScheduleItem, WeekScheduleItem


class DateScheduleItemSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = DateScheduleItem
        fields = ('id', 'temperature', 'start', 'end')


class WeekScheduleItemSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = WeekScheduleItem
        fields = ('id', 'temperature', 'day_of_week', 'start_time', 'end_time')
