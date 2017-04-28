from django.db import models
from django.utils.translation import ugettext_lazy as _

DAYS_OF_WEEK = (
    ('monday', _('Monday')),
    ('tuesday', _('Tuesday')),
    ('wednesday', _('Wednesday')),
    ('thursday', _('Thursday')),
    ('friday', _('Friday')),
    ('saturday', _('Saturday')),
    ('sunday', _('Sunday')),
)


class DateScheduleItem(models.Model):
    temperature = models.FloatField()
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return '{}-{}'.format(self.start, self.end)

    class Meta:
        verbose_name = _('date schedule item')
        verbose_name_plural = _('date schedule items')


class WeekScheduleItem(models.Model):
    temperature = models.FloatField()
    day_of_week = models.CharField(max_length=16, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return '{}: {}-{}'.format(self.day_of_week, self.start_time, self.end_time)

    class Meta:
        verbose_name = _('week schedule item')
        verbose_name_plural = _('week schedule items')
