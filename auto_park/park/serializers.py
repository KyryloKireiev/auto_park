from rest_framework import serializers
from .models import Driver

class DriverSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    driver_first_name = serializers.CharField(max_length=50)
    driver_last_name = serializers.CharField(max_length=50)
    drive_date = serializers.DateTimeField()

    def create(self, validated_data):
        return Driver.objects.create(**validated_data)






