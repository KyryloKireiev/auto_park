from rest_framework import serializers
from .models import Driver, Vehicle

class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = '__all__'


class VehicleSerializers(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'

class VehicleSetDriverSerializers(serializers.ModelSerializer):

#    id = serializers.Field(read_only=True)
#    driver = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#    make = serializers.CharField(read_only=True)
#    model = serializers.CharField(read_only=True)
#    plate_number = serializers.CharField(read_only=True)
#    created_at = serializers.DateTimeField(read_only=True)
#    updated_at = serializers.DateTimeField(read_only=True)


    class Meta:
        model = Vehicle
        fields = '__all__'


 #   class Meta:
 #       model = Vehicle
 #       fields = '__all__'
 #       read_only_fields = ('id', 'make', 'model', 'plate_number', 'created_at', 'updated_ad')


