from rest_framework import serializers
from .models import Driver

class DriverSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField()
    driver_first_name = serializers.CharField(write_only=True, max_length=50)
    driver_last_name = serializers.CharField(max_length=50)
    drive_date = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", write_only=True)

    class Meta:
        model = Driver
        fields = '__all__'

class DriverDetailSerializer(serializers.ModelSerializer):

    driver_first_name = serializers.CharField(max_length=50)
    driver_last_name = serializers.CharField(max_length=50)
    drive_date = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")

    class Meta:
        model = Driver
        fields = '__all__'



