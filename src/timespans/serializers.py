from rest_framework import serializers

from .models import Timespan


class TimespanSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Timespan
        fields = ('id', 'temperature', 'start', 'end')
        