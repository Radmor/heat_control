from django.contrib import admin
from .models import DateScheduleItem, WeekScheduleItem


@admin.register(DateScheduleItem)
class DateScheduleItemAdmin(admin.ModelAdmin):
    list_display = ('temperature', 'start', 'end')


@admin.register(WeekScheduleItem)
class WeekScheduleItemAdmin(admin.ModelAdmin):
    list_display = ('day_of_week', 'start_time', 'end_time')