from rest_framework import serializers
from .models import Driver, Vehicle


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = (
            "id",
            "driver",
            "make",
            "model",
            "plate_number",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "driver", "created_at", "updated_at")
