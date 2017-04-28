from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers

import schedule.api

router = routers.DefaultRouter()

router.register(
    'date_schedule', schedule.api.DateScheduleItemViewSet, 'date_schedule' 
)

router.register(
    'week_schedule', schedule.api.WeekScheduleItemViewSet, 'week_schedule'
)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)), 
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/temperature/', schedule.api.TemperatureViewSet.as_view(), name='temperature')
]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^rosetta/', include('rosetta.urls')),
    ]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
