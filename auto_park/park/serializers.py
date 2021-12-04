from rest_framework import serializers
from .models import Driver, Vehicle

#Создаем сериалайзер, который возвращает список фамилий водителей
# и позволяет создать нового водителя GET and POST
class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = '__all__'

#Создаем сериалайзер, который возвращает детальную инфу о водителе и позволяет
# редактировать и удалять водителя GET, UPDATE, DELETE
class DriverDetailCRUDSerializer(serializers.ModelSerializer):

#    id = serializers.IntegerField(read_only=True)
#    first_name = serializers.CharField(max_length=50)
#    last_name = serializers.CharField(max_length=50)
#    created_at = serializers.DateTimeField(read_only=True)
#    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Driver
        fields = '__all__'

#Создаем сериалайзер, который возвращает список автомобилей
# и позволяет создать нового водителя GET and POST

class VehicleSerializers(serializers.ModelSerializer):

#    id = serializers.IntegerField(read_only=True)
#    make = serializers.CharField(max_length=50)
#    model = serializers.CharField(max_length=50)
#    plate_number = serializers.CharField(max_length=50)
#    created_at = serializers.DateTimeField(read_only=True)
#    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Vehicle
        fields = '__all__'

#Создаем сериалайзер, который возвращает детальную инфу об автомобиле и позволяет
# редактировать и удалять автомобиль GET, UPDATE, DELETE

class VehicleDetailCRUDSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'


