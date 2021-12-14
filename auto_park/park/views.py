from datetime import datetime, timezone
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Driver, Vehicle
from .serializers import DriverSerializer, VehicleSerializer


class DriverListAPIView(ListCreateAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

    def get_queryset(self) -> QuerySet:
        queryset = Driver.objects

        if "created_at__lte" in self.request.GET:
            created_at__lte = datetime.strptime(
                self.request.GET.get("created_at__lte"), settings.DATE_INPUT_FORMAT
            ).replace(tzinfo=timezone.utc)
            queryset = queryset.filter(created_at__lte=created_at__lte)

        if "created_at__gte" in self.request.GET:
            created_at__gte = datetime.strptime(
                self.request.GET.get("created_at__gte"), settings.DATE_INPUT_FORMAT
            ).replace(tzinfo=timezone.utc)
            queryset = queryset.filter(created_at__gte=created_at__gte)

        return queryset


class DriverDetailCRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()
    lookup_field = "id"


class VehicleListAPIView(ListCreateAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()

    def get_queryset(self) -> QuerySet:
        queryset = Vehicle.objects.all()
        with_drivers = self.request.query_params.get("with_drivers")

        if with_drivers is not None and with_drivers not in {"yes", "no"}:
            raise ValidationError("Invalid value for parameter with_drivers")

        if with_drivers == "yes":
            queryset = queryset.filter(driver__isnull=False)
        if with_drivers == "no":
            queryset = queryset.filter(driver__isnull=True)

        return queryset


class VehicleDetailCRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    lookup_field = "id"


class SetVehicleDriverView(APIView):
    def post(self, request: Request, vehicle_id: int):
        driver_id = request.data["driver_id"]
        try:
            driver = Driver.objects.get(pk=driver_id)
            vehicle = Vehicle.objects.get(pk=vehicle_id)
        except ObjectDoesNotExist:
            return Response(status=404)

        if vehicle.driver:
            if vehicle.driver.id == driver_id:
                vehicle.driver = None
            else:
                return Response(status=409)
        else:
            vehicle.driver = driver

        vehicle.save()
        serialized = VehicleSerializer(vehicle)
        return Response(serialized.data)
