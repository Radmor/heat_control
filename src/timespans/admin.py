from django.contrib import admin
from .models import Timespan


@admin.register(Timespan)
class TimespanAdmin(admin.ModelAdmin):
    list_display = ('temperature', 'start', 'end')
    