from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView

import logging

from .models import Driver, Vehicle
from .serializers import DriverSerializer, VehicleSerializers, VehicleSetDriverSerializers

from datetime import datetime, timezone
from django.db.models import QuerySet
from django.conf import settings

class DriverListAPIView(ListCreateAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

    def get_queryset(self) -> QuerySet:
        queryset = Driver.objects

        if "created_at__lte" in self.request.GET:
            created_at__lte = datetime.strptime(self.request.GET.get("created_at__lte"),
                                                settings.DATE_INPUT_FORMAT).replace(tzinfo=timezone.utc)
            queryset = queryset.filter(created_at__lte=created_at__lte)

        if "created_at__gte" in self.request.GET:
            created_at__gte = datetime.strptime(self.request.GET.get("created_at__gte"),
                                                settings.DATE_INPUT_FORMAT).replace(tzinfo=timezone.utc)
            queryset = queryset.filter(created_at__gte=created_at__gte)

        return queryset


class DriverDetailCRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()
    lookup_field = 'id'


class VehicleListAPIView(ListCreateAPIView):
    serializer_class = VehicleSerializers
    queryset = Vehicle.objects.all()


    def get_queryset(self) -> QuerySet:
        queryset = Vehicle.objects.all()
        with_drivers = self.request.query_params.get('with_drivers')

        if with_drivers == 'yes':
            queryset = queryset.filter(driver__isnull=False)
        if with_drivers == 'no':
            queryset = queryset.filter(driver__isnull=True)
        return queryset


class VehicleDetailCRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializers
    queryset = Vehicle.objects.all()
    lookup_field = 'id'


class VehicleCreateDestroyDriverAPIView(RetrieveUpdateAPIView):
    serializer_class = VehicleSetDriverSerializers
    queryset = Vehicle.objects.all()
    lookup_field = 'id'
