from django.db import models
from django.utils.translation import ugettext_lazy as _

class Timespan(models.Model):
    temperature = models.FloatField()
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return '{}-{}'.format(self.start, self.end)

    class Meta:
        verbose_name = _('timespan')
        verbose_name_plural = _('timespans')
        