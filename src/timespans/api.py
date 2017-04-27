from rest_framework import viewsets, permissions

from .models import Timespan
from .serializers import TimespanSerializer


class TimespanViewSet(viewsets.ModelViewSet):
    serializer_class = TimespanSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Timespan.objects.all()
