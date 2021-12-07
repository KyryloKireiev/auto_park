from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.filters import SearchFilter
import logging

from .models import Driver, Vehicle
from .serializers import DriverSerializer, VehicleSerializers, VehicleSetDriverSerializers

from datetime import datetime, timezone
from .forms import DriverFilterForm
from rest_framework.request import Request
from rest_framework.response import Response
from typing import Any
from django.db.models import QuerySet
from django.conf import settings

class DriverListAPIView(ListCreateAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        form = DriverFilterForm(request.GET)
        if not form.is_valid():
            return Response(data=form.errors, status=400)
        return super().get(request, *args, **kwargs)

    def get_queryset(self) -> QuerySet:
        queryset = Driver.objects
        filter_fields = ["created_at__lte", "created_at__gte"]
        filter_kwargs = {}

        for field in filter_fields:
            if field in self.request.GET:
                datetime_ = datetime.strptime(self.request.GET[field], settings.DATE_INPUT_FORMAT)
                datetime_ = datetime_.replace(tzinfo=timezone.utc)
                filter_kwargs[field] = datetime_

        logging.warning(filter_kwargs)

        if filter_kwargs:
            queryset = queryset.filter(**filter_kwargs)

        return queryset


class DriverDetailCRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()
    lookup_field = 'id'


class VehicleListAPIView(ListCreateAPIView):
    serializer_class = VehicleSerializers
    queryset = Vehicle.objects.all()


    def get_queryset(self):
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


class VehicleCreateDestroyDriverAPIView(CreateAPIView):
    serializer_class = VehicleSetDriverSerializers
    queryset = Vehicle.objects.all()
    lookup_field = 'id'
